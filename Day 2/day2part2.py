with open('input.txt','r') as file:
    data = [i for i in file.read().strip().split("\n")]

"""Possible outcomes
A - Rock(1) : x - Loss
B - Paper(2) : y = Draw
c - Scissors(3) : z = Win
---------------------------------------------
A-X = 3+0 = 3
A-Y = 1+3 = 4
A-Z = 2+6 = 8
B-X = 1+0 = 1
B-Y = 2+3 = 5
B-Z = 3+6 = 9
C-X = 2+0 = 2
C-Y = 3+3 = 6
C-Z = 1+6 = 7

"""
second_results = {    
    "A X":3, "A Y":4, "A Z":8, 
    "B X":1, "B Y":5, "B Z":9,
    "C X":2, "C Y":6, "C Z":7
}

points = 0

for i in data:
    points += second_results[i]

print(points)