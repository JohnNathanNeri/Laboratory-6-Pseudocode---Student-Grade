name = input("Enter your name:")
print("Are you a member?\n Yes or No")
member = input("Are you member?")
age = int(input("Enter ypur age:"))

if age < 18:
    if member == "Yes":
        print("Your fee is 450.00 pesos")
    else:
        print("Your fee is 650.00 pesos")
elif age >= 18 and age <= 65:
    if member == "Yes":
        print("Your fee is 550.00 pesos")
    else:
        print("Your fee is 750 pesos")
elif age > 65:
    if member == "Yes":
        print("Your fee is 400 pesos")
    else:
        print("Your fee is 600.00 pesos")
