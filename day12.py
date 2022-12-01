input = open("input_day12.txt")

def checkPath(givenKey):
    for el in connections[givenKey]:
        if el in connectedToZero:
            return True
    return False


connections = {} #{0: [2], 1: [1], 2: [0, 3, 4], 3: [2, 4], 4: [2, 3, 6], 5: [6], 6: [4, 5]}
connectedToZeroCount = 0
connectedToZero = []
for line in input:
    numbers = ''.join(line.strip().split(' ')[2:])
    connections[int(line.strip().split(' ')[0])] = [int(x) for x in numbers.split(',')]

for key, value in connections.items():
    if key != 0:
        if key in connections[0]:
            connectedToZeroCount += 1
            connectedToZero.append(key)
        elif checkPath(key):
            connectedToZeroCount += 1
            connectedToZero.append(key)
        elif key in connectedToZero:
            connectedToZeroCount += 1
            connectedToZero.append(key)

#add zero
connectedToZeroCount+=1
print(connectedToZero)
print(connectedToZeroCount)
