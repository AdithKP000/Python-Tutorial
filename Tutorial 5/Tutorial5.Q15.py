""" 15. Write a code segment that prints the names of all of the items in the current working directory. """

import os

for item in os.listdir():
    print(item)
