# Program 12 - It's a program to print alphabet pattern


# Taking input of number of lines, jitni lines hame banani hai
lines = int(input("Enter number of lines: "))

# loop chlaayenge lines+1 tak
for i in range(1,lines): # isko 0 se shuru karnge
    # ab ek aur loop chalayenge ABCD... line se likhne ke liye number wale ke same ke jaise
    for j in range(i): # isme jitni line hai utne tak latter chalange
        print(chr(64+i),end="") # chr() function hai number ko alphabet me convert karne ke liye, 
                                # 65 character code se ABCD shuru hoti hai unicode me
    print("") # gap dene ke liye
