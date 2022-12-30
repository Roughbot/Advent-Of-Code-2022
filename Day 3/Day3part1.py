#day 3 Rucksack Problem
from string import ascii_letters

with open("day3data.txt") as file:
    data = [i for i in file.read().strip().split("\n")]

#Itrating through the data
sum = 0
for a in data:
    string = len(a)//2
    #seperating the string into right and left
    left = set(a[:string])
    right = set(a[string:])
    for key,char in enumerate(ascii_letters):
        #assigning ascii values for all the alphabets(capts and small) 
        if char in left and char in right:
            sum += key+1
print(sum)
    