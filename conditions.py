num=int(input("Enter your number:"))
if num >= 0:
    print("Positive number")
else:
    print("negative number")

Name=input("enter your name")
print("Hello", Name)
roll=int(input("enter your roll numbr:"))
if roll == 101:
    print("U are logged in")
else:
    print("Invalid roll number ")

Birth_year=int(input("Enter your bith year : "))
age= Birth_year - 2026 

print("Your age is ", age )

if age >= 18 :
    print("You are eligible to vote ")
else:
    print("You are not eligible to vote ")