# Import dependencies
import random
import sys

from labs.bin2dec import Bin2Dec

# Conversion methods
def decimalToBinary(n):
	return bin(n)[2:].replace("0b", "").zfill(8)

# Main function
def main(mode = "btd"):
	# Initialize validation flags
	check = []
	
	# Begin user input validation
	while len(check) != 3:
		rNum = random.randint(0, 255)
		while True:
			try:
				if mode == "btd":
					if (userInput := int(input(f"Convert {decimalToBinary(rNum)} to decimal: "))) == rNum:
						check.append(userInput)
						break
					else:
						print("Try again")
				elif mode == "dtb":
					if (userInput := int(input(f"Convert {rNum} to binary: "))) == decimalToBinary(rNum):
						check.append(userInput)
						break
					else:
						print("Try again")
				else:
					return print("Invalid mode selected.\nbtd = binary to decimal (default)\ndtb = decimal to binary")
			except ValueError:
				print("Bad input.")
	
	# Return flag
	return print(f"Your flag is: {hex(sum(check))}")

# Only run standalone
if __name__ == '__main__':
	Bin2Dec().lab()
	#main(*sys.argv[1:])
