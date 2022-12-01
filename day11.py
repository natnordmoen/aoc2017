input = open("input_day11.txt").read()
"""
for å kalkulere koordinater
NW|N |
--+--+--
SW|  |NE
--+--+--
  |S |SE
"""
x = 0
y = 0

distances = []

for direction in input.strip().split(","):
  if direction == "n":
    y += 1
  elif direction == "s":
    y -= 1
  elif direction == "ne":
    x += 1
  elif direction == "sw":
    x -= 1
  elif direction == "nw":
    x -= 1
    y += 1
  elif direction == "se":
    x += 1
    y -= 1
  distances.append((abs(x) + abs(y) + abs(x+y)) // 2)

print ("Part 1: ", (abs(x) + abs(y) + abs(x+y)) // 2)
print ("Part 2: ", max(distances))