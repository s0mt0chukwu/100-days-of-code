length= int(input("enter meter "))
unit = input("enter f or m")

if unit == "f":
    conversion = length * 0.3048
    print(f"your distance in meters is {conversion}")
elif unit == "m":
    conversion = length / 0.3048
    print(f"your distance in ft is {conversion}")
else:
    print("please enter f or m")
