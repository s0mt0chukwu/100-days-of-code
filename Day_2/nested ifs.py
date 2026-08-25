print("welcome to rollercoaster!")
height = int(input("enter your height in centimeters: "))
bill = 0
if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("enter your age: "))
    if age <= 12:
        bill = 5
        print('child ticket are $5')
    elif age <= 18:
        bill = 7
        print('youth ticket are $7')
    elif age >= 45 and age <= 55:
        print('Everything is going to be okay. Have a free ride on us')
    else:
        bill = 12
        print('adult ticket are $12')

    wants_photo = input("Do you want to have a picture take?  Type y for yes and n for no")
    if wants_photo == "y":
        #add $3 to their bill
        bill += 3

    print(f"your bill is ${bill}")
else:
    print('please you have to grow taller before you can ride')