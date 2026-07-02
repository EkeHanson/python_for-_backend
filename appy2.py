# Loop is the ability to do something again and again

name = None
while not name:
    name = input("Enter your name: ")

print(f"Welcome {name}!")

i = 3
while i != 0:
    print("MEOW!")

# FOR LOOP is a statement that 
# will execute it's block of code in a limited amount

for i in range(20, 30, 2):
    print(i)

# Count Down Timer
import time
for sec in range(10, 0, -1):
    print(sec)
    time.sleep(1)
print("Happy new Year!!!")


# NESTED FOR LOOPS: Loop inside another loop
rows = 4 # (0,1,2,3)
column = 5 # (0,1,2,3,4)
symbol = "#"
for i in range(rows):
    for j in range(column):
            print(symbol, end="")
    print()

for age in range(16, 20):
    if age == 18:
        break
    print("This is the age we are looking for")


for age in range(17, 21):
    if age == 17:
        continue
    print("You can vote")

def even(n):
    pass
import time
for i in range(20, 0, -1):
    if i % 2 == 0:
        continue
    print(i)
    time.sleep(1)