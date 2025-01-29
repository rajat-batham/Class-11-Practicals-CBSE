# Program 14 - It's a program to find factorial of any number


# Taking input for number
num = int(input("Enter number: "))

# ab factorial 1 hota default
factorial = 1
# ab loop se saare numbers ko input wale number tak multiply kar denge
for i in range(1,num+1):
    factorial = factorial * i

# ab print kar denge
print("Factorial: ",factorial)
