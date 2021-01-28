# Find the numbers

list = []

for value in range(1500,2700):
    if (value % 7 == 0) and (value % 5 == 0):
        list.extend([value])

print(list)
