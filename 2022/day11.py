import math, re


def monkey_play(rounds, calm):
    monkeys = {
        int(re.findall(r"\d+", m[0])[0]): {'items': list(map(int, re.findall(r"\d+", m[1]))), 'f': m[2].split('= ')[-1],
                                           'test': list(map(int, re.findall(r"\d+", m[3] + m[4] + m[5]))),
                                           'inspections': 0} for m in
        [m.split("\n") for m in open("day11.txt").read().split("\n\n")]}
    for r in range(rounds):
        for monkey in monkeys:
            while len(monkeys[monkey]['items']) > 0:
                monkeys[monkey]['inspections'] += 1
                if calm > 1:
                    worry = (lambda old: eval(monkeys[monkey]['f']))(monkeys[monkey]['items'].pop(0)) // calm
                else:
                    worry = (lambda old: eval(monkeys[monkey]['f']))(monkeys[monkey]['items'].pop(0)) % math.prod([m['test'][0] for m in monkeys.values()])
                if worry % monkeys[monkey]['test'][0] == 0:
                    monkeys[monkeys[monkey]['test'][1]]['items'].append(worry)
                else:
                    monkeys[monkeys[monkey]['test'][2]]['items'].append(worry)
    return math.prod(sorted([monkeys[m]['inspections'] for m in monkeys])[-2:])


if __name__ == "__main__":
    print(f"Part 1: {monkey_play(20, 3)}\nPart 2: {monkey_play(10000, 1)}")
