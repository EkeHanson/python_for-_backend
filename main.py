age = 1
a = 2

a = a + 1

#augmented assignment operator
a += 1

print(a)

#Data Types

#String
name = "Goodluck"

height, age, is_student = 34.32, 45, True
sponegbob = patrick = shandi = 34

print(type(name))
print(type(height))
print(type(age))
print(type(is_student))
print(patrick)
#You use the function
#  type to find the type of a vaiable


first_name = "Goodluck"
last_name = 'Goodluck'
print(f"my first name: {first_name} and last name:{last_name}")
#The triple quote is used 
# for multiline comment
comment = """ We just started 
the python class 
        for backend
 web development
"""
comment = ''' We just started 
the python class 
        for backend
 web development
'''

print(comment)

sentence = "My name is " + "Solomon"
print(sentence)

middle_name = "kIllion"
print(len(middle_name)) # The len function 
print(len(middle_name)) # The len function 
#finds the number of characters in a string
print(len(sentence))

surname = "  OKORO   "

#Find function
print(middle_name.find("o"))
print(middle_name.capitalize())
print(middle_name.upper())
print(middle_name.lower())

#Method chaaining
print(surname.strip().lower().capitalize())

print(surname.isdigit())
print(surname.isalpha())
print(surname.count("O"))
print(surname.replace("r", "o"))
#We want to change "Okoro" to "Ikiri"
print(surname.strip().lower().replace("o", "i").capitalize())

print(surname * 3)

#Type Casting
#THis is converting variable from one type to another
#INT => STR
#FLOAT => STR

age = 21
height = 23.45
age = str(age)
print(type(age))
sense1 = "I am " + str(height) + "cm tall"
print(sense1)
print(f"I am  {height}cm tall")

# Class Work
current_year =  "2026"
birth_year = 2010
#age = ?
#1. Convert current_year to an integer
current_year = int(current_year)
#2. Suntract birth_year from 
# current year assign the result to age
age = current_year - birth_year
#Print the result
print(f"age : {age}")

#ACcepting USer inputs
#We do that with the function input()
age = "23"
age = 23

# name = input("What is your name: ")
# age = input("How old are you: ")
# age = input("What is your height: ")

# print("Hello " + name + " !" + "you are" +  str(age) + " years old and your height is " + str(height) + "cm tall")

import math

print(math.pi)

print(round(math.pi))

print(math.floor(4.2))
print(math.ceil(4.2))
print(math.sqrt(81))

number1 = 23

# print(math.floor(number1))
# print(math.ceil(number1))

# print(max([1, 2, 3, 4, 5,6 ,67]))
# print(min([1, 2, 3, 4, 5,6 ,67]))

# print(pow(2, 3))

#STring Slicing
name = "Licoln"
# print(name[3])
#name[start:stop:step] last excluded
# print(name[0:5:1]) #Lico
# print(name[0:5]) #Lico
# print(name[::-1]) #Lico

website = "www.google.com"
first = website[0:9]
last = website[10:]
target = website[9:10].upper()
print(target)
print(first)
print(last)

new_website = first + target + last
print(new_website)

#Assignment 
#
# let a user enter a web address and print the company name
# www.google.com, www.facebook.com
#Google
#Facebook


