# Program 9 - It's a program to add numbers upto the input value


# Taking input of number, jaha tak hame add karna hai
num = int(input("Enter number: "))

# sum ko 0 kar denge
sum = 0

# ab loop se 0 se number tak ke saare number add kar denge
for i in range(num+1): #loop me last ke 1 pahle tak chalta hai, isliye num+1 tak karnege taaki poora num tak chale
    sum = sum + i # i --> 1,2,3,4,5,6,7,8,9,10.....
# ab sum ko print kar denge
print("The sum till",num,"is",sum)


