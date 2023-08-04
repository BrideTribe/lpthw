# import argv from sys module
from sys import argv

# pass a command line variable to argv
script, input_file = argv

# a function to print the content of a file
def print_all(f):
    print(f.read())

# a function to return our file to its original position
def rewind(f):
    f.seek(0)

# a function that print each line of the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# this read in the file and save it in a variable
current_file = open(input_file)

# print the content of the file
print("First let's print the whole file: \n")

print_all(current_file)

# rewind the file to the first position
print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines")
# set the current line, and print the first line of the file with the line numbers
current_line = 1 
print_a_line(current_line, current_file)

# increase the current line by 1
# set the current line, print the line number and the current line
current_line = current_line +1
print_a_line(current_line, current_file)

# increase the current line by 1
# set the current line, print the line number and the current line
current_line = current_line + 1
print_a_line(current_line, current_file)