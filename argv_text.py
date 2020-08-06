from sys import argv #it means from the module sys, import this function argv

script, filename = argv#defining the arguements

txt = open(filename)#this line gives a variable to open the text

print(f"Here's your file {filename}:")#the arguement is been printed
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
print(txt_again.close())
