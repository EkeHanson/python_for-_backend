a = 2
b = 3
c = a + b


x = 7
y = 4
z = x - y

l = 9
n = 3
m = l * n

q = 8
p = 3
r = q/p
s = q//p

divisor = 5
dividend = 17
modulus = dividend % divisor

base = 5
exponent = 3
result = base ** exponent # pow(5,3)

#IF STATEMENT
#It is a block of code that is 
# only executed when the statement is true

# age = int(input("Please enter your age: "))

# if age >=  100:
#     print("You are too old to vote")

# elif age >= 18:
#     print("Congrats!!! You can vote!")

# elif age <= 0:
#     print("You have not been born!!!")

# else:
#     print("Sorry! You are not eligible to vote!!")

#Write a program to determine if a number is an even or odd number

# number = int(input("Please enter the number: "))

# if number % 2 == 0:
#     print(f"Yes {number} is an even number")
# else:
#     print(f"No!, {number} is not an even number")

names = ["Nkechi", "Wale", "Dauda", "Ofiom", "Nteiro", "Iyalla"]
name = input("Please enter your name: ")
name = name.strip().lower().capitalize()

match name:
    case "Nkechi":
        print("You are Ibo")
    case "Wale":
        print("You are Yoruba")
    case "Dauda":
        print("You are Hausa")
    case "Ofiom":
        print("You are Ibibio")
    case "Nteiro":
        print("You are Obolo")
    case "Iyalla":
        print("You are Okrika")
    case _:
        print("Sorry I am not familiar with that")



#CLASS WORK
# Write a python program that will print "FOO" to the terminal 
# if the number is disivble by 3 and print "BOO" if the number
#is divible by 5 but it should print "FOOBOO" to the terminal 
#if the number  is divible by both  3 and 5



#Create a new file (quardratic_solver.py)
#Write a python program that will take the
#  coeficients of the equations variables and solve the equation
#ax^2 + bx + c = 0 e.g (x^2 - 5x + 6 = 0 )
#The program will ask for a, b and c respectively and give the values of x