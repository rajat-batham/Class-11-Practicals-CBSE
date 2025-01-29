# Program 8 - It's a program to check if a number is prime or not


# Taking input of number
num = int(input("Enter number: "))

# agar number 1 se bada hai to hi check karenge warna check nahi karenge
if num > 1:
    # ab number 1 se bada hoga to ye chalega warna nahi chalega
    # isme ab 2 se lekar ke jo number hai uske just 1 pahle tak check karenge ki uska remainder 1 hai ya nahi
    for i in range(2,(num)):
        # isme har num ko i se divide karke dekh rhe hain, agar remainder 0 aa rha hai to prime nahi hoga
        if (num%i)==0:
            print(num,"is not a prime")
            # jaise hi remainder 0 aayega, mtlb number prime nahi hai, print kar dega aur break ho jayega aur program band
            break
    # ye else loop ke liye hai, agar loop break nahi hota hai to ye condition chalge
    # mtlb ki agar 2 se lekar ke num-1 tak ke liye agar koi bhi remainder nahi hai to number prime hoga
    else:
        print(num,"is a prime")
# ye upar wale ke liye hai, agar number 1 se chota hoga to ye likh ke aayega 
else:
    print("Enter number greater than 1.")
