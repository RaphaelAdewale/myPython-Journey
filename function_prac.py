def human_being(name, age, location):
    print(f"My name is {name}.")
    print(f"I am {age} year old.")
    print(f"I live in {location}.")

print("Answer the following questions")
print("1. What is your name?")
name = input("> ")
print("2. How old are you?")
age =  int(input("> "))
print("3. Where do you live?")
location = input("> ")

print("\nThank you for your response.")
print("The following are your details:\n")

human_being(name, age, location)
