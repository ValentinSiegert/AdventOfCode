

if __name__ == '__main__':
    with open("day1.txt") as expenses_file:
        expenses = [int(line) for line in expenses_file.readlines()]
        found = False
        for cand1 in expenses:
            if found:
                break
            for cand2 in expenses:
                if cand1 + cand2 == 2020:
                    print(f'Real Expenses: {cand1*cand2}')
                    found = True
                    break




