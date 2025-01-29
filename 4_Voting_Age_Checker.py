# Program 4 - It's a program to find if a person with given age is eligible for voting or not


# Taking input of age
age = int(input("Enter your age: "))

# Checking if age is greater than 18 or equal to 18
if age >= 18:
    # then printing: you can vote
    print("You can vote!")
# If age is not greater than 18 then not eligible for voting
else:
    print("You can't vote!")


'''
Isko aur advance bayana jaa sakta hai pas abhi isme sirf if ya else use kar sakte hain, isliye ye 
bug dega. agar minus me bhi age daloge to no voting dikhegi, aur 1000 age bhi daloge to bhi eligible dikhoge
'''


