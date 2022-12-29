with open('part2.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

highest = []
sums = 0

for item in data:
    if item == "":
        highest.append(sums)
        sums = 0
    else:
        sums += int(item)

finalsum = 0
for i in range(3):
    finalsum += max(highest)
    highest.remove(max(highest))

print(finalsum)