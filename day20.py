input = open("input_day20.txt")

distances = {}
count = 0

def calcNewValues(coords, velocity, accel):
    velocity[0] += accel[0]
    velocity[1] += accel[1]
    velocity[2] += accel[2]
    coords[0] += velocity[0]
    coords[1] += velocity[1]
    coords[2] += velocity[2]
    return coords, velocity, accel


for line in input:
    distances[count] = []
    parts = line.strip().split(' ')
    coords = [int(i) for i in parts[0][3:-2].split(',')]
    velocity = [int(i) for i in parts[1][3:-2].split(',')]
    accel = [int(i) for i in parts[2][3:-1].split(',')]
    distances[count].append(sum([abs(i) for i in coords]))
    for x in range(1000):
        coords, velocity, accel = calcNewValues(coords, velocity, accel)
        distances[count].append(sum([abs(i) for i in coords]))
    count += 1

indices = []
i = 0
while i < 1000:
    valuesForStep = []
    for v in distances.values():
        valuesForStep.append(v[i])
    indices.append(valuesForStep.index(min(valuesForStep)))
    i+=1
print("PART 1: ", max(set(indices), key=indices.count))


#part 2
input.seek(0)

from collections import Counter
coordinates = {}
distances = {}
for line in input:
    distances[count] = []
    parts = line.strip().split(' ')
    coords = [int(i) for i in parts[0][3:-2].split(',')]
    velocity = [int(i) for i in parts[1][3:-2].split(',')]
    accel = [int(i) for i in parts[2][3:-1].split(',')]
    distances[count].extend((coords,velocity,accel))
    coordinates[count] = tuple(coords)
    count += 1

i = 0
while i < 500:
    for k,v in distances.items():
        v[0], v[1], v[2] = calcNewValues(v[0], v[1], v[2])
        coordinates[k] = tuple(v[0])
    c= Counter(coordinates.values())
    duplicated = []
    #check if any particles have collided
    for k,v in c.items():
        if v > 1:
            duplicated.append(k)
    #update distances - delete collided particles
    if len(duplicated) != 0:
        distances = {k:v for k,v in distances.items() if tuple(v[0]) not in duplicated}
    i+=1

print("PART 2: ", len(distances))