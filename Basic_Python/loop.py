expenses = [1200, 1500, 1300, 1700]
total = expenses[0] + expenses[1] + expenses[2] + expenses[3]
print(total)

total = 0
for e in expenses:
    total = total + e
print(total)

for i in range(len(expenses)):
    exp = expenses[i]
    print(f"Month {i+1}, expense: {exp}")
    total += exp

print("Total expenses: ", total)


for i in range(5, 10):
    print(i)

key_location = "chair"
locations = ["sofa", "garage", "chair", "table", "closet"]

for loc in locations:
    if loc == key_location:
        print("Found at: ", loc)
        break  # break the whole loop
    else:
        print("Not found at: ", loc)

print("Bye")


# print odd number between 1 to 10
for i in range(11):
    if i % 2 == 0:
        continue
    print(i)

n = 0
while n <= 10:
    print(n)
    n += 1