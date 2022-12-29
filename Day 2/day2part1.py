with open('input.txt','r') as file:
    data = [i for i in file.read().strip().split("\n")]

"""Possible outcomes
A - Rock - x
B - Paper - y
c - Scissors - z
---------------------------------------------
A-X = Draw = 1+3 = 4
A-Y = Win = 2+6 = 8
A-Z = Loss = 3+0 = 3
B-X = Loss = 1+0 = 1
B-Y = Draw = 2+3 = 5
B-Z = Win = 3+6 = 9
C-X = Win = 1+6 = 7
C-Y = Loss = 2+0 = 2
C-Z = Draww = 3+3 = 6

"""

results = {
    
    "A X":4, "A Y":8, "A Z":3, 
    "B X":1, "B Y":5, "B Z":9,
    "C X":7, "C Y":2, "C Z":6
}

points = 0

for i in data:
    points += results[i]

print(points)