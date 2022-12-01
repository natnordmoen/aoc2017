#part 1
steps = 356
buffer = [0]
curPos = 0
for i in range(1,2018):
    newPos = ((curPos + steps) % len(buffer))+1
    buffer.insert(newPos, i)
    curPos = newPos
print(buffer[curPos+1])

#part 2
#Zero is always at position 0, so we are interested in a value
#at position 1, no need to store the whole list
curLength = 1
curPos = 0
outValue = 0
for i in range(1,50000000):
    newPos = ((curPos + steps) % curLength)+1
    if newPos == 1:
        outValue = i
    curPos = newPos
    curLength += 1
print(outValue)