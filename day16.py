def spin(programs, number):
    spinned = ['a'] * len(programs)
    for index, value in enumerate(programs):
        spinned[(index + number) % len(programs)] = value
    return spinned


def exchange(pos1, pos2, programs):
    programs[pos1], programs[pos2] = programs[pos2], programs[pos1]
    return programs


def partner(prog1, prog2, programs):
    pos1, pos2 = programs.index(prog1), programs.index(prog2)
    programs[pos1], programs[pos2] = programs[pos2], programs[pos1]
    return programs


# programs = ['a','b','c', 'd', 'e']
# commands = ['s1','x3/4','pe/b']

programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
commands = open("input_day16.txt").read().strip().split(',')

# For part 1, comment till line 31 (start at line 35)

seen = []
for i in range(1000000000):
    seq = ''.join(programs)
    if seq in seen:
        print(seen[1000000000 % i])
        break
    seen.append(seq)

    for index, command in enumerate(commands):
        if command.startswith('s'):
            programs = spin(programs, int(command[1:]))
        elif command.startswith('x'):
            backslashIndex = command.index('/')
            programs = exchange(int(command[1:backslashIndex]), int(command[backslashIndex + 1:]), programs)
        elif command.startswith('p'):
            programs = partner(command[1], command[-1], programs)

    # print(''.join(programs))
