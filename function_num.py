def cheese_and_crackers(cheese_count, boxes_of_crackers): #i have define the function
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n") #anytime i callout cheese_and_crackers, this is what happens


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)#using the function straight up


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50 #represent the variable with another function

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6) #using numbers in the function


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #combining variable and numbers
