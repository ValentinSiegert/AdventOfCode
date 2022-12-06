import re

if __name__ == '__main__':
    stacks1, stacks2 = {}, {}
    rex1 = re.compile(r'(\s{3}|\[(?P<s>\w)\])\s')
    rex2 = re.compile(r'move\s(?P<a>\d*)\sfrom\s(?P<t1>\d*)\sto\s(?P<t2>\d*)')
    with open('day5.txt') as log_file:
        for line in log_file:
            for idx, match in enumerate(rex1.finditer(line)):
                if idx + 1 not in stacks1:
                    stacks1[idx + 1] = []
                    stacks2[idx + 1] = []
                if match.group('s'):
                    stacks1[idx + 1].insert(0, match.group('s'))
                    stacks2[idx + 1].insert(0, match.group('s'))
            if match2 := rex2.match(line):
                stacks1[int(match2.group("t2"))].extend(stacks1[int(match2.group("t1"))][:-int(match2.group("a"))-1:-1])
                stacks1[int(match2.group("t1"))] = stacks1[int(match2.group("t1"))][:-int(match2.group("a"))]
                stacks2[int(match2.group("t2"))].extend(stacks2[int(match2.group("t1"))][-int(match2.group("a")):])
                stacks2[int(match2.group("t1"))] = stacks2[int(match2.group("t1"))][:-int(match2.group("a"))]
    print(f"Part1: {''.join(s[-1] for s in stacks1.values())}")
    print(f"Part2: {''.join(s[-1] for s in stacks2.values())}")
