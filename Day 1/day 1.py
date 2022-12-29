with open('input.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

count = 0
max = 0
for i in data:
    if i == '':
        count = 0
    else:
        num = int(i)
        count += num

    if count > max:
        max = count

print(max)

