

s = open("input_day9.txt").read()
idx = 0

score_total = 0
uncanc = 0

stack = []
cscore = 0
garbage = False

while True:
    if idx >= len(s):
        break
    if s[idx] == "!":
        idx += 1
    elif garbage:
        if s[idx] == ">":
            garbage = False
        else:
            uncanc += 1
    elif s[idx] == "{":
        cscore += 1
        stack.append(cscore)
    elif s[idx] == "<":
        garbage = True
    elif s[idx] == "}":
        cscore -= 1
        score_total += stack.pop()
    idx += 1

print(score_total)
print(uncanc)
