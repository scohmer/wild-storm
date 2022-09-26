from src.num.numlabcore import NumberLabCore
from src.num.numlabflag import NumberLabFlagManager

class bin2dec(object):
    # Lab data function
    def lab_data(self):
        title = "Binary to Decimal"
        author = "Sean Cohmer, Cooper Violette"
        return title, author

    # Lab function
    def lab(self):
        # Initialize flag output check
        flagData = []

        # Begin user input validation
        while len(flagData) < 3:
            num = NumberLabCore.main(self, "bin", "dec")
            if (userInput := input(f"Convert {num[0]} to decimal: ")) == str(num[1]):
                flagData.append(int(userInput))
            else:
                print("Try again")

        # Return flag
        return print(f"Your flag is: {NumberLabFlagManager.main(self, flagData)}")
        

