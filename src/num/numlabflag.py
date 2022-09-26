class NumberLabFlagManager(object):
    def main(self, flagData = None):
        # Validate flag data
        if flagData is None:
            return "Library error in numlabflag.py: incorrect or missing flag data"
        
        # Continue flag data validation
        try:
            if len(flagData) != 3:
                return "Library error in numlabflag.py: incorrect flag data length"
        except:
            return "Library error in numlabflag.py: incorrect flag data type"

        # Format and return flag
        return "0x" + "{:02x}{:02x}{:02x}".format(*flagData).upper()