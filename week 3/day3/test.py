# Open the file in read mode ("r")
with open("text.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
