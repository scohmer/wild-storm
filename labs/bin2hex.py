from src.num.numlabcore import NumberLabCore
from src.num.numlabflag import NumberLabFlagManager

class bin2dec(object):
    # Lab data function
    def lab_data(self):
        title = "Binary to Hexadecimal"
        author = "Cooper Violette"
        return title, author

    # Lab function
    def lab(self):
        # Initialize flag output check
        flagData = []

        # Begin user input validation
        while len(flagData) < 3:
            num = NumberLabCore.main(self, "bin", "hex")
            if (userInput := input(f"Convert {num[0]} to hexadecimal: 0x").upper()) == str(num[1]):
                flagData.append(int(userInput))
            else:
                print("Try again")

        # Return flag
        return print(f"Your flag is: {NumberLabFlagManager.main(self, flagData)}")
        

