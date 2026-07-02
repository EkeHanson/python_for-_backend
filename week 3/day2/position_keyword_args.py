# Comparison of Positiona and Keyword Arguements

def sum(num1, num2):
    total_sum = num1 + num2
    return total_sum

print(sum(12, 78))

def greet(first, height=23.4, age=10):
    print(f"Hello {first} you are {height}cm tall and {age} years old! Welcome to our class")


# greet("Killion")
# greet("Jersy", 34, 67)
# greet("Nket", height=15.7)
greet("Martias", age=84, height=15.7)