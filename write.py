from sys import argv#this is a delicate code
#do not run it anyhow, be careful
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")#there was actually no need for this
print("If you do want that, hit RETURN.")#and this too

input("?")

print("Opening the file...")
target = open(filename, 'w')#what was the function of the "w"

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")
raph = (line1, line2, line3)
target.write(raph)
formatter = "{} {} {}"
print(formatter.format(line1, line2, line3))

print("And finally, we close it.")
target.close()

from sys import argv

script, filename = argv
txt = open(filename)
print(txt.read())
