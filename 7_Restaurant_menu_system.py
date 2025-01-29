# Program 7 - It's a program to calculate the user's bill according to menu


# sabse pahle user ka bill 0 kar denge
bill = 0
# fir repeat ko True kar denge agar repeat karne wala banana hai to 
repeat = True

# fir while loop me code ko likhenge, aur akhri me pooch lenge agar aur add karna hai to aur add kar denge warna repeat ko False kar denge
while repeat == True:
    # a poora menu likh lo 
    print("Welcome to Rassi Da Dhaba, Give your order from menu")
    print("------------------MENU-------------------") # ye sirf acchaa dikhane ke liye hai
    # yaha ha se main hai
    print("1. Pizza: RS 299")
    print("2. Coffee: RS 99")
    print("3. Burger: RS 99")
    print("4. French Fries: RS 49")
    print("5. Chai: RS 11")
    print("") # ek khali line accha dikhane ke liye
    # ab user se choise lenge ki kya lena hai usko, wahi number daale
    choice = int(input("Choose your item as 1,2,3,4 or 5: "))
    # ab condition daalenge sabki, jo select karenge utna uske bill me add kar denge
    if choice == 1:
        bill = bill + 299 # bill me hi add karna hai isliye bill + 299 kiya
    if choice == 2:
        bill = bill + 99
    if choice == 3:
        bill = bill + 99
    if choice == 4:
        bill = bill + 49
    if choice == 5:
        bill = bill + 11    
    # ab bill print kar denge
    print("Bill: ",bill)
    # ab user se input lenge Y ya N me, agar Y select karega to repeap True hoga, agar N karege to repeat nahi hoga aur code khatm ho jayeg
    user_repeat = input("Do you want to add more in the bill ?\nType 'Y' for Yes and 'N' for No':  ")
    if user_repeat == "Y" or "y":
        repeat = True
    if user_repeat == "N" or "n":
        repeat = False

# ab code khatm kar denge
print("Thanks for coming!")




