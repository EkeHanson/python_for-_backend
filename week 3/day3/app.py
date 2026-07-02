import csv

staff = []

with open("C:/Users/Ekene-onwon/Desktop/Codes/Python/week 3/day3/index.csv", "r") as file:
    reader = csv.reader(file, delimiter=";")

    for row in reader:
        if not row:
            continue
            
        if len(row) == 5:
            ID, Name, Department, Salary, Hire_Date = row
            print(ID, Name, Department, Salary, Hire_Date)
        else:
            print(f"Skipping invalid row: {row}")
