import random

class NumberLabCore(object):    
    def main(self, start = None, end = None):
        # Validate lab flags
        if start is None or end is None or start == end or start not in ["bin","hex","dec"] or end not in ["bin","hex","dec"]:
            return "Library error in numlabcore.py: incorrect syntax"

        # Initialize output values
        output = []

        # Calculate random value
        rNum = random.randint(0, 255)

        # Append formatted random value to output
        if start == "bin":
            output.append(bin(rNum)[2:].replace("0b", "").zfill(8))
        elif start == "dec":
            output.append(rNum)
        elif start == "hex":
            output.append(hex(rNum))
            
        # Append expected conversion value to output
        if end == "bin":
            output.append(bin(rNum)[2:].replace("0b", "").zfill(8))
        elif end == "dec":
            output.append(rNum)
        elif end == "hex":
            output.append(hex(rNum))

        # Return output
        return output