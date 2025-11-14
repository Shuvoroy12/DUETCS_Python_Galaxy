'''Task 1: Take a student's marks as input and print their grade using comparison and
conditional statements.'''

Number=float(input())


if Number>80:
    print("Your Grade is A+ and Grade point is 4.00")
elif Number>=75 and Number<80:
    print("Your Grade is A and Grade point is 3.75")
elif Number>=70 and Number<75:
    print("Your Grade is A- and Grade point is 3.50")
elif Number>=65 and Number<70:
    print("Your Grade is B+ and Grade point is 3.25")
elif Number>=60 and Number<65:
    print("Your Grade is B and Grade point is 3.00")
elif Number>=55 and Number<60:
    print("Your Grade is B- and Grade point is 2.75")
elif Number>=50 and Number<55:
    print("Your Grade is C+ and Grade point is 2.50")
elif Number>=45 and Number<50:
    print("Your Grade is C and Grade point is 2.25")
elif Number>=40 and Number<45:
    print("Your Grade is D and Grade point is 2.00")
else :
    print("Your are Fail")



'''Task2:  Ask the user to enter a number and determine whether it’s even or
odd using a conditional statement.'''


Number=int(input("Enter the number ="))


if Number==0 or Number==1:
    print("Your number is none ",Number)
elif Number%2==0:
    print("Your number is Even")
else :
    print("Your number is Odd")


'''Task3 Check word length : Ask the user to enter a word and: -> 
Print “Short word” if it’s less than 5 characters->Print “Medium word” 
if it’s between 5 and 8 -> Print “Long word” if it’s more than 8 characters'''

W_length=input("Enter your word=")
length=len(W_length)

if length<5:
    print("Short word")
elif length>=5 and length<=8:
    print("Medium word")
elif length>8:
    print("Long word")




'''Task 4:— Password Strength Checker : Take a password from the user and 
check:-> If it’s less than 6 characters → print “Weak password”->
If it contains spaces → print “Invalid password”-> If it’s 6–10
characters → print “Medium password” -> If it’s more than 10 → print “Strong password”'''

Password=input("Enter your password =")
length=len(Password)
Sp_count= Password.count(" ")

if Sp_count>0:
    print("Not a valid password")
elif length<6:
    print("Weak password")
elif length>=6 and length<=10 :
    print("Medium password")
elif length>10:
    print("Strong Password")


'''Task 5 — Name Formatter :  Ask the user for their name, then:-> Remove
extra spaces-> Capitalize the first letter-> Display the cleaned name'''

Name=input("Enter the name =")
Name=Name.replace(" ","")
Name=Name.capitalize()
# Name=Name.strip()
print(Name) 



'''Task 6 — Username Validator: Write a program that asks for a username and checks:->
Must not be empty-> Must not contain spaces-> Must be at least 4 characters'''

Name=input("Enter your name =")
length=len(Name)
sp_count=Name.count(" ")
if length<4 or sp_count>0:
    print("Username not valid")
else :
    print("Username is valid")
 