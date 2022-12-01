input = open("input_day4.txt", "r")


#task 1
valid = 0
for line in input:
    words = line.split()
    unique_words=set(words)
    if len(words) == len(unique_words):
        valid+=1
print(valid)

#short version
input.seek(0)
print(len([line for line in input if len(line.split()) == len(set(line.split()))]))

#nullstill for å lese fra starten
input.seek(0)

#task 2
valid_2 = 0
for line in input:
    sortedWords = []
    for w in line.split():
        sortedWords.append(''.join(sorted(w)))
    if len(sortedWords) == len(set(sortedWords)):
        valid_2+=1
print(valid_2)
