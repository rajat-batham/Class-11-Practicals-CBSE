# Program 11 - It's a program to print number pattern


# Taking input of number of lines, jitni lines hame banani hai
lines = int(input("Enter number of lines: "))

# loop chlaayenge lines+1 tak
for i in range(lines+1): # isko 0 se shuru karnge
    num = 1
    # ab ek aur loop chalange jo 1234.. sabme 1 add karke
    for i in range(i+1): # isme jitne lines hai utne hi number add honge
        print(num,end="") # end="" krange to new line me nahi jaata, isko hataoge to har number alag line me aayega
        num = num + 1 # ab har baar num me 1 add kar denge
    print("") # ye har 123.. wali line ke baad gap dene ke liye

