from itertools import islice

if __name__ == '__main__':
    with open('day3.txt') as log_file:
        prio_sum = group_sum = 0
        iter_lf = iter(log_file)
        reached_end = False
        while not reached_end:
            try:
                line1, line2, line3 = islice(iter_lf, 3)
                prio_num = lambda c: ord(c) - 38 if c.isupper() else ord(c) - 96
                line_set = lambda l: ''.join(set(l[:len(l)//2]).intersection(l[len(l)//2:]))
                prio_sum += prio_num(line_set(line1)) + prio_num(line_set(line2)) + prio_num(line_set(line3))
                group_sum += prio_num(''.join(set(line1.strip()).intersection(line2.strip()).intersection(line3.strip())))
            except ValueError:
                reached_end = True
    print(f"Part1: {prio_sum}")
    print(f"Part2: {group_sum}")
