input = open("input_day8.txt", "r")

def changeReg(action, register, dif):
    if action == 'inc':
        registers[register] += dif
    else:
        registers[register] -= dif

registers = {}

for line in input:
    elements = line.split(' ')
    if elements[0] not in registers.keys():
        registers[elements[0]] = 0


input.seek(0)
maxValue = 0
for line in input:
    elements = line.split(' ')
    register = elements[0]
    dif = int(elements[2])
    condReg = elements[4]
    condition = elements[5]
    condInt = int(elements[6])
    if condition == '>':
        if registers[condReg] > condInt:
            changeReg(elements[1], register, dif)
            if max(registers.values()) > maxValue:
                maxValue = max(registers.values())
    elif condition == '<':
        if registers[condReg] < condInt:
            changeReg(elements[1], register, dif)
            if max(registers.values()) > maxValue:
                maxValue = max(registers.values())
    elif condition == '<=':
        if registers[condReg] <= condInt:
            changeReg(elements[1], register, dif)
            if max(registers.values()) > maxValue:
                maxValue = max(registers.values())
    elif condition == '>=':
        if registers[condReg] >= condInt:
            changeReg(elements[1], register, dif)
            if max(registers.values()) > maxValue:
                maxValue = max(registers.values())
    elif condition == '==':
        if registers[condReg] == condInt:
            changeReg(elements[1], register, dif)
            if max(registers.values()) > maxValue:
                maxValue = max(registers.values())
    elif condition == '!=':
        if registers[condReg] != condInt:
            changeReg(elements[1], register, dif)
            if max(registers.values()) > maxValue:
                maxValue = max(registers.values())

#task 1
print(max(registers.values()))

#task 2
print(maxValue)