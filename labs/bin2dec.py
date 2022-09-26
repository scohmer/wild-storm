from src.numlabcore import NumberLabCore

class Bin2Dec(object):
    def __init__(self, *args, **kwargs):
        self.title = "Binary to Decimal"
        self.author = "Sean Cohmer, Cooper Violette"

    def lab(self):
        print(NumberLabCore.main(self, "bin", "dec"))
