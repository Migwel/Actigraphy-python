import argparse
import sys
from processes import *
from constantes import *


def main(argv):
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('-i', '--indiv')
	group.add_argument('-c', '--comp')
	group.add_argument('-g', '--group')
	args = parser.parse_args()
	print args

	if args.indiv:
		process_indiv(args.indiv)
	elif args.comp:
		process_comp(args.comp)
	elif args.group:
		process_group(args.group)

if __name__ == "__main__":
	main(sys.argv[1:])
