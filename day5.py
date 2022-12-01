input = open("input_day5.txt", "r")
numbers = []
for number in input:
    numbers.append(int(number))


#task 1
jumps = 0
nextIndex = 0
#numbers=[0,3,0,1,-3] #test array from the task
while nextIndex < len(numbers):
    thisNumber = numbers[nextIndex]
    numbers[nextIndex] += 1
    nextIndex += thisNumber
    jumps += 1

print(jumps)

# remember to reset numbers (or comment out part 1)


#task 2
jumps = 0
nextIndex = 0
#numbers=[0,3,0,1,-3]
while nextIndex < len(numbers):
    thisNumber = numbers[nextIndex]
    if thisNumber >= 3:
        numbers[nextIndex] -= 1
    else:
        numbers[nextIndex] += 1
    nextIndex += thisNumber
    jumps += 1

print(jumps)