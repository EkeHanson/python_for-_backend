#FUNCTION - This is a block of code that is only executed when it is called.
def even():
    num = 23 #int(input("Please anter the number: "))
    if num % 2 == 0:
        print(f"{num} is an even number!")
    else:
        print(f"{num} is not even")
def greet(name):
    print(f"Hello {name} you are welcome to our class")
# Multiply the sum to their difference with two functions: 3 and 5 = 16
def sum(num1, num2):
    total_sum = num1 + num2
    return total_sum
def diff(num1, num2):
    total_diff = num1 - num2
    return total_diff

sum(5, 3)
diff(5, 3)
# print(8 * 2)
total = sum(5,3) * diff(5, 3)
print(total)

#Write a python function that can be used to calcualte 
# the simple interest(I) on a Principal(P) given a rate(R) in a time(T)
                # Simple Interest Formula
                #       P * T * R
                # SI = ───────────
                #          100

# where,
# P = Principal
# R = Rate of Interest in % per annum
# T = Time (number of years)
#The Time, Rate and Principal are to be accepted from the user on the  terminal