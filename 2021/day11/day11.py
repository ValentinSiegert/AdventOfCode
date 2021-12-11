
def print_octopuses(octs):
    for line in octs:
        print(''.join(map(str, line)))
    print('')


def flash_octopus(octs, y, x, flash):
    octs[y][x] = 0
    flash += 1
    ads = [(y-1, x, y - 1 >= 0), (y + 1, x, y + 1 < len(octs)), (y, x - 1, x - 1 >= 0),
           (y, x + 1, x + 1 < len(octs[y])), (y - 1, x - 1, y - 1 >= 0 and x - 1 >= 0),
           (y - 1, x + 1, y - 1 >= 0 and x + 1 < len(octs[y])), (y + 1, x - 1, y + 1 < len(octs) and x - 1 >= 0),
           (y + 1, x + 1, y + 1 < len(octs) and x + 1 < len(octs[y]))]
    for y1, x1, cond in ads:
        if cond:
            octs[y1][x1] += 1 if octs[y1][x1] != 0 else 0
            if octs[y1][x1] > 9:
                flash = flash_octopus(octs, y1, x1, flash)
    return flash


if __name__ == '__main__':
    print_it = False
    octopuses = [[i for i in map(int, line.strip())] for line in open('day11.txt').readlines()]
    flashes = 0
    steps = 100
    step = 1
    all_flashed = False
    while step <= steps or not all_flashed:
        octopuses = [[i + 1 for i in line] for line in octopuses]
        for y0, row in enumerate(octopuses):
            for x0, o in enumerate(row):
                if o > 9:
                    flashes = flash_octopus(octopuses, y0, x0, flashes)
        print_it and print(f'After step {step}:')
        print_it and print_octopuses(octopuses)
        if step == steps:
            print(f'Total flashes after {steps} steps are {flashes}.\n')
        if any([[i for i in line if i > 0] for line in octopuses]):
            step += 1
        else:
            all_flashed = True
            print(f'The first step during which all octopuses flash is {step}.\n')

