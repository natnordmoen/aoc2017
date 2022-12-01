f = open("day2_input.txt")
input = []
for line in f.readlines():
    input.append([int(i) for i in line.split()])

part1 = 0
for l in input:
    part1 += max(l) - min(l)

# short
print(sum(max(l) - min(l) for l in input))

sum_task_2 = 0
for l in input:
    for ix1, number in enumerate(l):
        for ix2, number2 in enumerate(l):
            if ix1 != ix2 and number % number2 == 0:
                    sum_task_2 += number // number2

print(sum_task_2)
