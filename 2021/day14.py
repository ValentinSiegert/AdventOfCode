from collections import Counter, defaultdict

if __name__ == '__main__':
    steps = 40
    with open('day14.txt') as logfile:
        poly, rules = logfile.read().split('\n\n')
        rules = {c1 + c2: tuple([e, c1 + e, e + c2]) for c1, c2, *_, e in rules.split('\n')}
    char_counter = Counter(poly)
    pair_counter = Counter(''.join(pair) for pair in zip(poly, poly[1:]))
    for step in range(1, steps + 1):
        new_p = defaultdict(int)
        for pair, total in pair_counter.items():
            element, pair1, pair2 = rules[pair]
            char_counter[element] += total
            new_p[pair1] += total
            new_p[pair2] += total
        pair_counter = new_p
    print(f'Quantity of the most common element - Quantity of the least common element = '
          f'{max(char_counter.values()) - min(char_counter.values())}')

