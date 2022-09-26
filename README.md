# Wild Storm
A lab creation framework written in Python, designed to be simple and scalable for teacher assignment creation / student assignment completion.

## How to use
Simply run the `wild-storm.py` script directly, ensuring the required subdirectories are accessible.

``python wild-storm.py``

By default, the script will prompt the user to select which lab they want to do. To skip this menu and run labs directly, pass the filename of the lab as an argument. For example, to load the Decimal to Binary lab (included with this software), you would run:

``python wild-storm.py dec2bin.py``

**Requires Python 3.8 or higher.**

## Documentation
Labs are very simple to create. All lab scripts follow 3 simple guidelines:

1. All labs must have a class that matches the file name exactly. **The next two guidelines must be within this class.**
2. All lab classes must have a `lab_data` function that returns a title and author value.
3. All lab classes must have a `lab` function. This function is what runs when the lab is loaded.

Following these guidelines should result in a file that looks like this:
```
# myepiclab.py

class myepiclab(object):
    def lab_data(self):
        title = "My Epic Lab"
        author = "mpxf"
        return title, author
    
    def lab(self):
        <lab code here>

<other classes / imports can be placed outside of the main class>
```
