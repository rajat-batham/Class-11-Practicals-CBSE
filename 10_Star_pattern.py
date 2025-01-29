# Program 10 - It's a program to print star pattern


# Taking input of number of lines, jitni lines hame banani hai
lines = int(input("Enter number of lines: "))

# loop chlaayenge lines+1 tak
for i in range(1,lines+1): # isko 1 se shuuru karnge warna pahle line khali print hogi, 0 se multiply hone pe
    # ab star ko print karenge aur multiply kar denge line{i} se
    print("*"*i)


