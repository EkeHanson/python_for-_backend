utensils = {"Fork", "Spoon", "Cup", "Knife"}

# for utensil in utensils:
#     print(utensil)
# utensils.add("Napkin")
# utensils.remove("Knife")
# utensils.clear()
dishes = {"Bowl", "Plate", "Cup"}

# utensils.update(dishes)
# print(utensils)

#Union is the combination of two separate set
dinner_table = utensils.union(dishes)
# print(dinner_table)

diff = utensils.difference(dishes)
# print(diff)


intersect = utensils.intersection(dishes)
print(intersect)