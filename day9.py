import re
#input = open("little_input_day9.txt")
input = open("input_day9.txt")
newLines = []


#match = re.match(r"[^!]<.*([^1]>)", line)
newLine = re.sub(r'\!.{1}','', input.read().strip() )
newer = re.sub(r'<(.*)>', '', newLine)
newLines.append(newer)

print(newLines)
