

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
    print(f"Points: {points}")
    print(f"Score: {score}")
