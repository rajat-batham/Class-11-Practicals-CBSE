# Program 5 - It's a program to find percentage of marks and give grade according to percentage


# Input for student name
name = input("Enter your name: ") # isme sirf input() use kiya kyuki name lena tha, number nahi
# Input for roll number
roll_no = int(input("Enter your roll number: "))

print("Enter number out of 100") # isme 100 me se calculate karnege, 80 me se bhi kar sakte formule me change karna padega bas

# Har subject ke marks input kar lenge
# float(input()) use karenge, kyuki kisi ke .5 me bhi number hote hain  
math_marks = float(input("Enter your Maths marks: "))
english_marks = float(input("Enter your English marks: "))
chemistry_marks = float(input("Enter your Chemistry marks: "))
physics_marks = float(input("Enter your Physics marks: "))
cs_marks = float(input("Enter your Computer Science marks: "))

# total marks add kar lenge
total_marks = math_marks + english_marks + chemistry_marks + physics_marks + cs_marks

# ab percentage nikalenge sabki milake
# jo bracket me hota hai wo sabse pahle calulate hota hai for uske bahar wale bracket wala calucalte hoga, aise chalta hai
percentage = (total_marks//500) * 100 # isme floor division{//} use kar rhe hain, approximate value ke liye, 
                                      # warna point me kabhi kabhi bahut lambi value aati hai

# ab saare grade ki condition daalenge
# 1 - agar percentage 90% tak ya us se jyada hai to A grade hai (question me bolega kya karna, 90 tak rakhna hai ya 90 se jyada, agar 90 se jyada rakhna hai to sirf > use karnge, warna >= karenge)
if percentage >= 90:
    # fir grade variable bana ke usme grade ko likh denge
    grade = "A"
# 2 - agar percentage 90% se neeche hai aur 80% tak hai to B grade hai
elif percentage < 90 and percentage >= 80:
    grade = "B"
# 3 - agar percentage 80% se neeche hai aur 70% tak hai to C grade hai
elif percentage < 80 and percentage >= 70:
    grade = "C"
# 4 - agar percentage 70% se neeche hai aur 50% tak hai to D grade hai
elif percentage < 70 and percentage >= 50:
    grade = "D"
# 5 - agar percentage 50% se neeche hai aur 33% tak hai to E grade haikyuki 33% pe pass hote hain 
elif percentage < 50 and percentage >= 33:
    grade = "E"
# 6 - agar percentage 33% se neeche hai to fail, isme else bhi use kar sakte hai koi problem nahi
else:
    grade = "F"

# beech me space dene ke liye ek khali print bhi chala sakte ho
print("")

# aakhri me sabkuch print kar denge - name, roll no, percentage aur grade
print("Name: ",name)
print("Roll number: ",roll_no)
print("Percentage: ",percentage)
print("Grade: ",grade)