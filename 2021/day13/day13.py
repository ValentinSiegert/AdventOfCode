
if __name__ == '__main__':
    with open('day13.txt') as logfile:
        dots, manual = logfile.read().split('\n\n')
        dots = {tuple([d for d in map(int, ds.split(','))]) for ds in dots.split('\n')}
        manual = [tuple([ms.split('=')[0].split()[2], int(ms.split('=')[1])]) for ms in manual.split('\n')]
    folding = 1
    for fold, line in manual:
        new_dots = set()
        for dot in dots:
            new_x = dot[0]
            new_y = dot[1]
            if fold == 'y':
                if dot[1] < line:
                    new_y = dot[1]
                elif dot[1] == line:
                    continue
                else:
                    new_y = line - (dot[1] - line)
            else:
                if dot[0] < line:
                    new_x = dot[0]
                elif dot[1] == line:
                    continue
                else:
                    new_x = line - (dot[0] - line)
            new_dots.add(tuple([new_x, new_y]))
        dots = new_dots
        print(f'After completing {folding} instructions, there are {len(dots)} points left.')
        folding += 1
    print('')
    screen = [['.' for x in range(0, max(dots, key=lambda e: e[0])[0] + 1)] for y in range(0, max(dots, key=lambda e: e[1])[1] + 1)]
    for dot in dots:
        screen[dot[1]][dot[0]] = '#'
    for line in screen:
        print(''.join(line))
