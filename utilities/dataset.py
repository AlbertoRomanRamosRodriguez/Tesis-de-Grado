import shutil
import random

from general import log
from os import listdir
from os.path import join

def zipDataset(ZIP_NAME: str, DATASET_PATH:str):

    shutil.make_archive(ZIP_NAME, 'zip', DATASET_PATH)
    log(f"[ZIPPED] {ZIP_NAME} ready to ship to Colab")

def exportLabel(label: str, output_f_name: str, expt_path: str):
	"""
	Exports label corresponding to the image
	"""
	label_file = join(expt_path, f'{output_f_name}.txt')
	with open(label_file, 'w') as f:
		f.write(label)

	log(f"[EXPORTED LABEL]")

def getTrainingAndTest( elements: list, total_bd_elements: int, TRAIN_IMGS_PATH, TRAINING_FACTOR):

	ratio = len(listdir(TRAIN_IMGS_PATH)) / total_bd_elements
	factor = TRAINING_FACTOR - ratio # % of non-analyzed images to send to training set

	training = random.sample(elements, int(len(elements)*factor))
	test = [g for g in elements if g not in training]

	return (training,test)