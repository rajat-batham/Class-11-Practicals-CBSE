# Program 15 - It's a program to check if a string is palindrome


# pahle sentence ya word ko input kar lenge
sen = input("Enter your charater: ")

# ab ek empty list bannayenge
list1 = []

# ab loop se sentence ke saare words ko list me daal denge aapend karke
for i in sen:
    list1.append(i)

# ab check kar lenge kya sidhi list se ulti list match ho rahi hai ya nahi, agar ha to same hai, agar nahi to nahi
if list1 == list1[::-1]:
    print("It's Palindrome")
else:
    print("Not Palindrome")


