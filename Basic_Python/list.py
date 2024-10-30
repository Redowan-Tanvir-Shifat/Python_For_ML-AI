mithai = ["kheer", "halva", "jalebi", "gulab jamun"]  # creating list
# print(type(mithai))
# print(mithai[1:3])  # slicing

mithai.append("laddu")  # add new item at last
# print(mithai)

mithai.insert(2, "kulfi")  # add new item at any index
# print(mithai)

tikha = ["samosa", "sev"]
food = mithai + tikha  # add to list
# print(food)

mithai[0] = "kalojam"  # change item at any index
# print(mithai)

# print(dir(mithai))  # to know exist funtions for the list mithai

# print(mithai)
mithai.reverse()  # to reverse the list
# print(mithai)