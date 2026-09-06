print("welcome to Python Pizza deliveries!")
size = input("what size do you want? S,M or L: ")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("you typed the wrong input")
    exit()

pepperoni = input("Do you want pepperoni on your Pizza? y or n: ")
if pepperoni == "y":
    if size == "S":
        bill += 2
    else:
        bill += 3

extra_cheese = input("Do you want extra cheese? y or n: ")
if extra_cheese == "y":
    bill += 1

print(f"your final bill is ${bill}" )