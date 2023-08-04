# import an 'argv' from a 'sys' module
from sys import argv

# create an argument variable
script, filename = argv

# open filename into var txt
txt = open(filename)

# read the content contained in the filename
print(f"Here's your file {filename}:")
print(txt.read())

# close the file
txt.close()

# receives the file name again
print("Type the filename again:")
file_again = input("> ")

# open filename into txt_again
txt_again = open(file_again)

# print the content of the file
print(txt_again.read())

# close file
txt_again.close()