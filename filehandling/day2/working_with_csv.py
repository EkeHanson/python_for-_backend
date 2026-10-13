# with open("house.csv", "rt") as file:
#     for line in file:
#         print(line.strip())




# with open("house.csv", "rt") as file:
#     for line in file:
#         id, name, house = line.strip().split(",")
#         if name == "name":
#             continue
#         print(f"{name} belongs to {house}")

import csv

with open("house.csv", "rt") as file:
    reader = csv.reader(file)
    for row in reader:
        if not row or row[0] == "id":
            continue
        id, name, house = (c.strip() for c in row)
        print(f"{name} belongs to {house}")


writer = csv.writer(open("house.csv", "a", newline=""))
writer.writerow([4, "Roberth", "Baratheon"])
writer.writerow([5, "Jon Snow", "Stark"])