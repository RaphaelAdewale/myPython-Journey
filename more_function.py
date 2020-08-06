from sys import argv #import argv from the system

script, input_file = argv #don't forget to run two the values

def print_all(f):# defining the functions
    print(f.read()) #read the filename

def rewind(f): #make the code non-working
    f.seek(0) # look for a cerain line of code

def print_a_line(line_count, f):
    print(line_count, f.readline()) #at a particular number, read that line1

current_file = open(input_file) #defining a variables

print("First let's print the whole file:\n")

print_all(current_file) # read the filename

print("Now let's rewind, kind of like a tape.")

rewind(current_file) #doesnt show the file

print("Let's print three lines:")

current_line = 1 #defines a variable
print_a_line(current_line, current_file) #read a specific line

current_line = 2
print_a_line(current_line, current_file)

current_line = 3
print_a_line(current_line, current_file)
