# Program 6 - It's a program to find greatest number from 3 given numbers


# Taking input for three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# pahle ham number 1 ko bada maan lenge
great_num = num1

# ab num1 ko compare karenge num2 aur num3 se, agar num2 num1 se bada hoga to change kar denge, 
# agar num3 num1 se bada hoga to usko change kar denge, agar num1 kisi se bhi bada nahi hai to num1 hi sabse bada hoga
if num2 > great_num:
    great_num = num2
if num3 > great_num:
    great_num = num3 

# ab bade number ko print kar denge
print("Greatest number is: ",great_num)

