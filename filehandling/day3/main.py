import json

with open("data.json") as f:
    data = json.load(f)

print(data)
print(data["name"])      
print(data["courses"][0])

# print(data["school"]["email"])
email = data.get("school", {}).get("email1", "No email found")
print(email)


data = {"name": "Bob", "age": 25}

with open("output.json", "w") as f:
    json.dump(data, f, indent=4)


student = {
    "name": "Chidi",
    "age": 22,
    "city": "Lagos",
    "greeting": "Ẹ káàbọ̀",  
    "course": "Python"
}

with open("output.json", "w") as f:
    json.dump(student, f, indent=4, sort_keys=True, ensure_ascii=False)

import json

s = '{"name": "Zara", "age": 22}'
data = json.loads(s)         
print(data["name"])  
