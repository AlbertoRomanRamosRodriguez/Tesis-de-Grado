from os import path, listdir
from utilities.dataset import zipDataset, getTrainingAndTest
from utilities.general import checkPathExists


datasets = [f for f in listdir() if f.isupper()]
for i, d in enumerate(datasets):
    print(f"{i} - {d}")

BD_PATH = path.join(datasets[int(input("\nSelect Dataset: "))])
DATASET_PATH = path.join('Dataset')
checkPathExists(DATASET_PATH)

TRAIN_PATH = path.join(DATASET_PATH, 'train')
checkPathExists(TRAIN_PATH)
TRAIN_IMG_PATH = path.join(TRAIN_PATH, 'images')
checkPathExists(TRAIN_IMG_PATH)
TRAIN_MASK_PATH = path.join(TRAIN_PATH, 'masks')
checkPathExists(TRAIN_MASK_PATH)

TEST_PATH = path.join(DATASET_PATH, 'test')
checkPathExists(TEST_PATH)
TEST_IMG_PATH = path.join(TEST_PATH, 'images')
checkPathExists(TEST_IMG_PATH)
TEST_MASK_PATH = path.join(TEST_PATH, 'masks')
checkPathExists(TEST_MASK_PATH)