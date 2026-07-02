# An Exception is any event detetcted during a 
# program execution so it does not affect the execution of the program

try:
    x = float(input("Enter the numerator: "))
    y = float(input("Enter the denominator: "))
    z = y/x
    print(z)
except ZeroDivisionError as e:
    print("You cannot divide by zero")

except ValueError as e:
    print("Please enter only numers")

except Exception as e:
    print(e)



