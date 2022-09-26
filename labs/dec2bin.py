from src.num.numlabcore import NumberLabCore
from src.num.numlabflag import NumberLabFlagManager

class dec2bin(object):
    # Lab data function
    def lab_data(self):
        title = "Decimal to Binary"
        author = "Sean Cohmer, Cooper Violette"
        return title, author

    # Lab function
    def lab(self):
        # Initialize flag output check
        flagData = []

        # Begin user input validation
        while len(flagData) < 3:
            num = NumberLabCore.main(self, "dec", "bin")
            if (userInput := input(f"Convert {str(num[0])} to binary: ")) == str(num[1]):
                flagData.append(int(userInput, 2))
            else:
                print("Try again")

        # Return flag
        return print(f"Your flag is: {NumberLabFlagManager.main(self, flagData)}")
        

