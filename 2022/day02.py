

if __name__ == '__main__':
    points = score = 0
    with open('day2.txt') as log_file:
        for line in log_file:
            one, two = line.strip().split()
            one, two = ord(one) - 64, ord(two) - 87
            if one == two:
                points += 3
            elif (one+1) % 3 == two % 3:
                points += 6
            points += two
            if two == 2:
                score += 3
            elif two == 3:
                score += 6
            score += 3 if (one + two + 1) % 3 == 0 else (one + two + 1) % 3
    print(f"Part1: {points}")
    print(f"Part2: {score}")
    # short version
    print(f"Part1: {sum((3 + to) if (oo:= ord(o) - 64) == (to:= ord(t) - 87) else (6 + to) if (oo + 1) % 3 == to % 3 else (0 + to) for o, t in (l.strip().split() for l in open('day2.txt')))}")
    print(f"Part2: {sum((3+(3 if ((fo:=ord(f)-64)+so+1)%3==0 else (fo+so+1)%3)) if (so:= ord(s) - 87) == 2 else (6 + (3 if ((fo:=ord(f)-64)+so+1)%3==0 else (fo+so+1)%3)) if so == 3 else (0 + (3 if ((fo:=ord(f)-64)+so+1)%3==0 else (fo+so+1)%3)) for f, s in (r.strip().split() for r in open('day2.txt')))}")