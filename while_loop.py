
def loop(b, c):
    a = 0
    numbers = []
    while a < b:
        print(f"At the top a is {a}")
        numbers.append(a)

        a = a + c
        print("Numbers now: ", numbers)
        print(f"At the bottom a is {a}")

loop(8, 2)

a = 0
numbers = []
while a < 6:
    print(f"At the top a is {a}")
    numbers.append(a)

    a = a + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom a is {a}")


print("The numbers: ")

for num in numbers:
    print(num)
