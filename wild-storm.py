# Import dependencies
import sys

# Import local dependencies
from src.lab_loader import LabLoader

# Only run standalone
if __name__ == '__main__':
	print("Wild Storm Labs")
	print("===============")
	LabLoader().main(*sys.argv[1:])
