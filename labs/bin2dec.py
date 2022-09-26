from src.numlabcore import NumberLabCore

class Bin2Dec(object):
    def __init__(self, *args, **kwargs):
        self.title = "Binary to Decimal"
        self.author = "Sean Cohmer, Cooper Violette"

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
        return print(f"Your flag is: {hex(sum(flagData))}")
        

