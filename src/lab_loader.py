import os
import importlib

class LabLoader(object):
    def main(self, directFile = None):
        # Ensure lab directory exists
        if not os.path.exists("labs"):
            return print("Library error in lab_loader.py: labs directory does not exist")

        # Create lab caching variable
        labs = []

        # Load all labs from lab directory
        for lab in os.listdir(os.path.relpath("labs")):
            if lab[-3:] == ".py":
                try:
                    lab_import = importlib.import_module(f"labs.{lab[:-3]}")
                    lab_data = getattr(lab_import, lab[:-3])
                    title, author = lab_data.lab_data(self)
                    labs.append({"title": title, "author": author, "import_class": lab_data})
                except:
                    print(f"Failed to load {lab}, verify it contains valid lab data and try again.")

        # Create lab selection menu
        print("")
        for i in range(len(labs)):
            print(f"{i + 1}. {labs[i]['title']} (by {labs[i]['author']})")
        print("")

        # Create user input
        while True:
            try:
                userInput = int(input("Enter the desired lab number to begin: "))
                return labs[userInput - 1]["import_class"].lab(self)
            except:
                pass



                
