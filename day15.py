genA = [634]
genB = [301]

#For å teste
#genA = [65]
#genB = [8921]

factA = 16807
factB = 48271

divider = 2147483647

#part 1

count = 0
while count != 40000000:
    nextA = (genA[count]*factA)%divider
    nextB = (genB[count]*factB)%divider
    genA.append(nextA)
    genB.append(nextB)
    count += 1

print("Calculated 40 mill pairs")
countAlike = 0
for a, b in zip(genA[1:], genB[1:]):
    binA = str(bin(a))[-16:]
    binB = str(bin(b))[-16:]
    if binA == binB:
        countAlike += 1
print(countAlike)

#part 2
count = 0
forJudgeA = []
forJudgeB = []

while count != 50000000:
    nextA = (genA[count]*factA)%divider
    nextB = (genB[count]*factB)%divider
    genA.append(nextA)
    genB.append(nextB)
    count += 1
    if len(forJudgeA) < 5000000 and nextA % 4 == 0:
        forJudgeA.append(nextA)
    if len(forJudgeB) < 5000000 and nextB % 8 == 0:
        forJudgeB.append(nextB)
    if len(forJudgeA) == 5000000 and len(forJudgeB) == 5000000:
        break

print("Calculated 5 mill pairs", " For a: ", len(forJudgeA), " For b: ", len(forJudgeB))
countAlike = 0
for a, b in zip(forJudgeA, forJudgeB):
    binA = str(bin(a))[-16:]
    binB = str(bin(b))[-16:]
    if binA == binB:
        countAlike += 1
print(countAlike)


