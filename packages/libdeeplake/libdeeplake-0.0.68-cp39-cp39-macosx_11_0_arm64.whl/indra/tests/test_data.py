from indra import api
from indra.pytorch.loader import Loader
from .constants import MNIST_DS_NAME, COCO_DS_NAME
import numpy as np
import deeplake
import math
from deeplake.util.exceptions import TokenPermissionError
import pytest
from .utils import tmp_datasets_dir, data_path
import numcodecs.lz4
import pickle
import random
import string

CHECKOUT_TEST_NAME = "checkout_directory"
SEQUENCE_DS_NAME = "sequence_dataset"
LZ4_COMPRESED_DATA_DIR = "lz4_compressed_dataset"
LZ4_SHAPES_ENCODER = "lz4_sample_compresses"
LZ4_CHUNK_COMPRESSON_SHAPES_ENCODER = "lz4_chunk_compression_shapes_encoder"


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def test_chunk_compressed_chunk_shape_encoder_bps_encoder_matches(tmp_datasets_dir):
    """
    Checkec correct reading of sahpes encoder and bytes position encoder
    for chunk compressed chunks
    """
    ds = deeplake.dataset(
        tmp_datasets_dir / LZ4_CHUNK_COMPRESSON_SHAPES_ENCODER, overwrite=True
    )
    with ds:
        ds.create_tensor(
            "tokens",
            "text",
            chunk_compression="lz4",
        )
    for i in range(1000):
        ds.tokens.append(get_random_string(i))

    cpp_ds = api.dataset(str(tmp_datasets_dir / LZ4_CHUNK_COMPRESSON_SHAPES_ENCODER))
    assert len(cpp_ds) == len(ds) == 1000
    for i in range(1000):
        assert cpp_ds.tokens[i].numpy() == ds.tokens[i].numpy()


def test_samples_compressed_chunk_shape_encoder_bps_encoder_matches(tmp_datasets_dir):
    """
    Checkec correct reading of sahpes encoder and bytes position encoder
    bytes position encoder shows the sample bytes positon in the chunks
    as during sample compesesion compressed bytes of different shapes can be equal
    we need to meake sure that we are anyways correctly interpreating those cases
    """
    with open(data_path("first_element.bin"), "rb") as f:
        first = pickle.load(f)

    with open(data_path("second_element.bin"), "rb") as f:
        second = pickle.load(f)

    assert first.shape == (390,)
    assert second.shape == (374,)

    first_compressed = numcodecs.lz4.compress(first.tobytes())
    second_compressed = numcodecs.lz4.compress(second.tobytes())
    assert len(first_compressed) == len(second_compressed)

    tmp_ds = deeplake.dataset(tmp_datasets_dir / LZ4_SHAPES_ENCODER, overwrite=True)
    with tmp_ds as ds:
        ds.create_tensor(
            "tokens",
            dtype="uint16",
            sample_compression="lz4",
        )
    tmp_ds.tokens.append(first)
    tmp_ds.tokens.append(second)
    cpp_ds = api.dataset(str(tmp_datasets_dir / LZ4_SHAPES_ENCODER))
    assert len(cpp_ds) == 2
    assert cpp_ds.tokens[0].shape == tmp_ds.tokens[0].shape
    assert cpp_ds.tensors[0][1].shape == tmp_ds.tokens[1].shape


def test_lz4_compressed_data_read(tmp_datasets_dir):
    """
    check lz4 compressed data read
    """
    tmp_ds = deeplake.dataset(tmp_datasets_dir / LZ4_COMPRESED_DATA_DIR, overwrite=True)
    with tmp_ds as ds:
        ds.create_tensor(
            "tokens",
            htype="generic",
            dtype="uint16",
            sample_compression="lz4",
        )
        ds.create_tensor(
            "images",
            htype="image",
            dtype="uint8",
            sample_compression="lz4",
        )
        for _ in range(1000):  # 1000 random data
            random_data = np.random.randint(0, 256, (100, 10), dtype=np.uint16)
            ds.tokens.append(random_data)
        for _ in range(1000):  # 1000 random images
            random_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
            ds.images.append(random_data)
    ds.flush()
    assert len(ds) == 1000

    cpp_ds = api.dataset(str(tmp_datasets_dir / LZ4_COMPRESED_DATA_DIR))
    assert len(cpp_ds) == 1000
    for i in range(1000):
        assert np.array_equal(cpp_ds.tokens[i].numpy(), ds.tokens[i].numpy())
        assert np.array_equal(cpp_ds.images[i].numpy(), ds.images[i].numpy())


def test_sequential_dataset(tmp_datasets_dir):
    """
    check sequence dataset element handling
    """
    tmp_ds = deeplake.dataset(tmp_datasets_dir / SEQUENCE_DS_NAME, overwrite=True)
    with tmp_ds as ds:
        ds.create_tensor("seq", htype="sequence[class_label]")
        ds.create_tensor("seq_labels", htype="sequence[class_label]")

    ds.seq.append(["l1", "l2", "l3"])
    ds.seq_labels.append(
        [["ship", "train", "car"], ["ship", "train"], ["car", "train"]]
    )
    ds.flush()

    ds2 = api.dataset(str(tmp_datasets_dir / SEQUENCE_DS_NAME))
    assert len(ds2) == 1
    assert ds2.tensors[0].name == "seq"
    assert len(ds2.tensors[0][0].numpy()) == 3
    assert len(ds2.tensors[1][0].numpy()) == 3
    for cpp, dp in zip(ds2.tensors[1][0].numpy(), ds.seq_labels[0].numpy(aslist=True)):
        assert np.array_equal(cpp, dp)

    for cpp, dp in zip(ds2.tensors[0][0].numpy(), ds.seq[0].numpy(aslist=True)):
        assert np.array_equal(cpp, dp)


def test_sequence_dataset(tmp_datasets_dir):
    """
    check sequence dataset element handling, with decompression
    """
    ds = deeplake.dataset(tmp_datasets_dir / "sequence_decompression")
    shape = (13, 17, 3)
    arrs = np.random.randint(0, 256, (5, *shape), dtype=np.uint8)
    ds.create_tensor("x", htype="sequence[image]", sample_compression="png")
    ds.x.append(arrs)

    cpp_ds = api.dataset(str(tmp_datasets_dir / "sequence_decompression"))
    data1 = cpp_ds.tensors[0][0].numpy()
    data2 = ds.x[0].numpy()
    assert len(data1) == len(data2) == 5

    for a, b in zip(data1, data2):
        assert np.array_equal(a, b)


def test_coco_bmasks_equality():
    """
    check binary masks consitency for coco_train dataset
    """
    cpp_ds = api.dataset(COCO_DS_NAME)[0:100]
    hub_ds = deeplake.load(COCO_DS_NAME, read_only=True, verbose=False)[0:100]

    assert len(cpp_ds) == len(hub_ds)
    assert cpp_ds.tensors[2].name == "masks"
    assert cpp_ds.tensors[0].name == "images"
    for i in range(100):
        assert np.array_equal(hub_ds.masks[i].numpy(), cpp_ds.tensors[2][i].numpy())
        assert hub_ds.images[i].numpy().shape == cpp_ds.tensors[0][i].numpy().shape
        assert hub_ds.images[i].numpy().shape == cpp_ds.images[i].numpy().shape


def test_mnist_images_equality():
    cpp_ds = api.dataset(MNIST_DS_NAME)[0:100]
    hub_ds = deeplake.load(MNIST_DS_NAME, read_only=True, verbose=False)[0:100]

    assert len(cpp_ds) == len(hub_ds)
    assert cpp_ds.tensors[0].name == "images"
    for i in range(100):
        assert np.array_equal(hub_ds.images[i].numpy(), cpp_ds.tensors[0][i].numpy())

    assert cpp_ds.tensors[1].name == "labels"
    for i in range(100):
        assert np.array_equal(hub_ds.images[i].numpy(), cpp_ds.tensors[0][i].numpy())


def test_hub_dataset_pickling():
    ds = api.dataset(MNIST_DS_NAME)
    before = len(ds)
    pickled_ds = pickle.dumps(ds)
    new_ds = pickle.loads(pickled_ds)
    after = len(new_ds)
    assert after == before
    assert new_ds.path == ds.path


@pytest.mark.outdated
def test_s3_sliced_dataset_pickling():
    ds = api.dataset(MNIST_DS_NAME)[0:1000]
    ds = ds[1:100]
    pickled_ds = pickle.dumps(ds)
    new_ds = pickle.loads(pickled_ds)
    assert len(new_ds) == len(ds)
    assert new_ds.path == ds.path

    ds = new_ds[[0, 12, 14, 15, 30, 50, 60, 70, 71, 72, 72, 76]]
    before = len(ds)
    pickled_ds = pickle.dumps(ds)
    unpickled_ds = pickle.loads(pickled_ds)
    assert len(unpickled_ds) == len(ds) == 12


def test_hub_sliced_dataset_pickling():
    ds = api.dataset(MNIST_DS_NAME)[0:1000]
    ds = ds[1:100]
    pickled_ds = pickle.dumps(ds)
    new_ds = pickle.loads(pickled_ds)
    assert len(new_ds) == len(ds)
    assert new_ds.path == ds.path

    ds = new_ds[[0, 12, 14, 15, 30, 50, 60, 70, 71, 72, 72, 76]]
    pickled_ds = pickle.dumps(ds)
    unpickled_ds = pickle.loads(pickled_ds)
    assert len(unpickled_ds) == len(ds) == 12


def test_pickleing():
    ds = api.dataset(MNIST_DS_NAME)
    l_ds = ds[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    pickled_ds = pickle.dumps(l_ds)
    another = pickle.loads(pickled_ds)
    assert len(another) == 10

    s_ds = ds[1:1000]
    pickled_ds = pickle.dumps(s_ds)
    another = pickle.loads(pickled_ds)
    assert len(another) == 999

    s_ds = s_ds[10:300]
    pickled_ds = pickle.dumps(s_ds)
    another = pickle.loads(pickled_ds)
    assert len(another) == 290

    s_ds = s_ds[10:30]
    pickled_ds = pickle.dumps(s_ds)
    another = pickle.loads(pickled_ds)
    assert len(another) == 20


def test_dataset_slicing():
    ds = api.dataset(MNIST_DS_NAME)[0:100]
    assert len(ds) == 100

    ds1 = ds[[0, 7, 10, 6, 7]]
    assert len(ds1) == 5
    with pytest.raises(IndexError):
        ds2 = ds1[[7],]


def test_checkout_with_ongoing_hash(tmp_datasets_dir):
    ds = deeplake.dataset(tmp_datasets_dir / CHECKOUT_TEST_NAME, overwrite=True)
    with ds:
        ds.create_tensor("image")
        ds.image.extend(([i * np.ones((i + 1, i + 1)) for i in range(16)]))
        ds.commit()
        ds.create_tensor("image2")
        ds.image2.extend(np.array([i * np.ones((12, 12)) for i in range(16)]))

    commit_id = ds.pending_commit_id
    ds2 = api.dataset(str(tmp_datasets_dir / CHECKOUT_TEST_NAME))
    ds2.checkout(commit_id)


def test_return_index():
    indices = [0, 10, 100, 11, 43, 98, 40, 400, 30, 50]
    ds = api.dataset(MNIST_DS_NAME)[indices]

    ld = ds.loader(batch_size=1, return_index=True)
    it = iter(ld)

    for idx, item in zip(indices, it):
        assert idx == item[0]["index"]


def test_polygon_data(tmp_datasets_dir):
    ds = deeplake.dataset(tmp_datasets_dir / "polygon_dataset", overwrite=True)
    with ds:
        ds.create_tensor(
            "polygon",
            dtype=np.float32,
            htype="polygon",
            sample_compression=None,
        )
        for i in range(10):
            polygons = []
            for j in range(i):
                p = np.ndarray((3 + j, 2))
                c = (3 + j) / 2
                for k in range(3 + j):
                    p[k] = [
                        200 * (j % 3) + 150 * (math.sin(6.28 * k / (3 + j)) + 1) / 2,
                        200 * (j / 3) + 150 * (math.cos(6.28 * k / (3 + j)) + 1) / 2,
                    ]
                polygons.append(p)
            ds.polygon.append(polygons)

    ids = api.dataset(str(tmp_datasets_dir / "polygon_dataset"))
    for i in range(10):
        assert len(ids.tensors[0][i].numpy()) == i


def test_bytes(tmp_datasets_dir):
    ds = deeplake.dataset(tmp_datasets_dir / "bytes_test_dataset", overwrite=True)
    with ds:
        ds.create_tensor(
            "images",
            dtype=np.uint8,
            htype="image",
            sample_compression="jpeg",
        )
        ds.create_tensor(
            "images_meta",
            htype="json",
        )
        ds.create_tensor(
            "json_tensor",
            htype="json",
            chunk_compression="lz4",
        )
        ds.create_tensor(
            "labels",
            htype="sequence[class_label]",
        )
        for i in range(10):
            ds.images.append(np.random.randint(0, 255, (100, 100, 3), np.uint8))
            ds.images_meta.append({"index": i})
            ds.json_tensor.append({"index": i})
            ds.labels.append([i, i + 1, i + 2])

    ids = api.dataset(str(tmp_datasets_dir / "bytes_test_dataset"))
    for i in range(10):
        assert ids.images[i].bytes() == ds.images[i].tobytes()
        assert ids.images_meta[i].bytes() == ds.images_meta[i].tobytes()
        assert ids.json_tensor[i].bytes() == ds.images_meta[i].tobytes()
        assert b"".join(ids.labels[i].bytes()) == ds.labels[i].tobytes()


def test_empty_dataset(tmp_datasets_dir):
    ds = deeplake.dataset(tmp_datasets_dir / "empty_tensors_dataset", overwrite=True)
    with ds:
        ds.create_tensor(
            "labels",
            htype="class_label",
        )

    ids = api.dataset(str(tmp_datasets_dir / "empty_tensors_dataset"))
    view = ids.query("SELECT * WHERE false")
    assert ids.labels.numpy().shape == (0,)
    assert ids.labels.numpy(aslist=True) == []
    assert ids.labels.bytes() == b""
    assert view.labels.numpy().shape == (0,)
    assert view.labels.numpy(aslist=True) == []
    assert view.labels.bytes() == b""
