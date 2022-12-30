#day 3 Rucksack Problem
from string import ascii_letters

with open("day3data.txt") as file:
    data = [i for i in file.read().strip().split("\n")]

j = 3
sum = 0
for i in range(0,len(data), 3):
    string2 = data[i:j]
    j += 3

    for key,char in enumerate(ascii_letters):
        if char in string2[0] and char in string2[1] and char in string2[2]:
            sum += key +1
    

print(sum)
