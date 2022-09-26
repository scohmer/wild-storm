from src.num.numlabcore import NumberLabCore
from src.num.numlabflag import NumberLabFlagManager

class hex2dec(object):
    # Lab data function
    def lab_data(self):
        title = "Hexadecimal to Decimal"
        author = "Cooper Violette"
        return title, author

    # Lab function
    def lab(self):
        # Initialize flag output check
        flagData = []

        # Begin user input validation
        while len(flagData) < 3:
            num = NumberLabCore.main(self, "hex", "dec")
            if (userInput := input(f"Convert {str(num[0])} to decimal: ")) == str(num[1]):
                flagData.append(int(userInput))
            else:
                print("Try again")

        # Return flag
        return print(f"Your flag is: {NumberLabFlagManager.main(self, flagData)}")
        

