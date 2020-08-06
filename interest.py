def interest(principal, rate, time):
    print(principal * rate % time )


print("I will now calculate your simple interest:")
print("What is your principal?")
principal = float(input(">"))
print("What is the interest rate?")
rate = float(input(">"))
print("How long would you borrow the money")
time = float(input(">"))

interest(principal, rate, time)
