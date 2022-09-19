from os.path import join, exists
from os import mkdir

def checkPathExists(PATH: str):
    if not exists(PATH):
     mkdir(PATH)

def log(msg: str, LOGS_PATH: str, LOGS_F: str):
	"""
		Prints the msg on the console and stores the log file
	"""
	print(msg)
	with open(join(LOGS_PATH, LOGS_F), "a") as f:
		f.write(msg + '\n')

def end_of_process(msg: str):
	log(msg)
	exit()