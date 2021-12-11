
if __name__ == '__main__':
    unc = 0
    total = 0
    with open('day8.txt') as log_file:
        for line in log_file:
            patterns, output = line.strip().split('|')
            output = output.strip().split()
            patterns = patterns.strip().split()
            numbers = ['' for i in range(0, 10)]
            sixes = []
            fives = []
            for p in patterns:
                sorted_p = ''.join(sorted(p))
                if len(p) == 2:
                    numbers[1] = sorted_p
                elif len(p) == 3:
                    numbers[7] = sorted_p
                elif len(p) == 4:
                    numbers[4] = sorted_p
                elif len(p) == 7:
                    numbers[8] = sorted_p
                elif len(p) == 6:
                    sixes.append(sorted_p)
                else:
                    fives.append(sorted_p)
            for s in sixes:
                if not set(numbers[1]) <= set(s):
                    numbers[6] = s
                elif set(numbers[4]) <= set(s):
                    numbers[9] = s
                else:
                    numbers[0] = s
            for f in fives:
                if set(numbers[7]) <= set(f):
                    numbers[3] = f
                elif set(f) <= set(numbers[6]):
                    numbers[5] = f
                else:
                    numbers[2] = f
            fn = ''
            for value in output:
                unc += 1 if len(value) <= 4 or len(value) == 7 else 0
                fn += str(numbers.index(''.join(sorted(value))))
            total += int(fn)
    print(f'There exist a total of {unc} unique numbers.')
    print(f'The total if all output values is: {total}')
