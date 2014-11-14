from acti_functions import *
from constantes import *

def process_indiv(fileName):
	print "PROCESS INDIV"
	
	try:
		readActiFile(fileName)
	except Exception as exc:
		print exc

	print "PROCESS INDIV-END"


def process_comp(fileName):
	print "PROCESS COMP"

	try:
		readActiFile(fileName)
	except Exception as exc:
		print exc

	print "PROCESS COMP-END"

def process_group(dirName):
	print "PROCESS GROUP ("+dirName+")"
	print "PROCESS GROUP-END"
