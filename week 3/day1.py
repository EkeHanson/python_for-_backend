#Dictionaries - is a  of changeable, unordered collection of unique key : values pairs
#They are fast because they use hashing, and allow us tioo access values quickly

capitals = {"USA": "Washington DC", "Nigeria": "Abuja", "Japan": "Tokyo" }
# print(capitals["Nigeria"])
# print(capitals.get("Nigeria"))
# print(capitals["South Africa"])Accra
# print(capitals.get("South Africa"))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.get("Ghana"), "Accra")

# for key, value in capitals.items():
#     print(key, ":" , value)

capitals.update({"Rwanda": "Kigali"})
# print(capitals.items())

capitals.pop("USA")
capitals.clear()
print(capitals.items())

# WHy Dictionary - avoid multiple lists
# students = ["Hermione", "Harry", "Ron", "Draco"]
# house = ["Greyfindoor", "Greyfindoor", "Greyfindoor", "Slytherin"]

numbers = {
  "1": "One",  "2": "Two",  "3": "Three",  "4": "Four",  "5": "Five", 
 "6": "Six",  "7": "Seven",  "8": "Eight",  "9": "Nine",  "10": "Ten"
}

number = input("Enter the digit btw 1 and 10: ")

for key, value in numbers.items():
    if number == key:
        print(f"The number you entered is called: {value}")
       
    
"😂" = "Smile"
"❤" = "Love"
"🤣" = "Laugh"
"✔" = "Good"
"✌ "= "Peace"
"👍" = "OK"
"🤦‍♂️" = "Tired"
