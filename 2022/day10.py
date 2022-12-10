def cycling(c, x, s, p):
    p[c//40] += '#' if c % 40 in range(x-1, x+2) else '.'
    c += 1
    if c in s.keys():
        s[c] = c*x
    return c, s


if __name__ == "__main__":
    cycle, X, saves, crt = 0, 1, {i: 0 for i in range(20, 260, 40)}, ['' for j in range(6)]
    with open("day10.txt") as f:
        for ln in f:
            cmd = ln.split()
            cycle, saves = cycling(cycle, X, saves, crt)
            if cmd[0] == "addx":
                cycle, saves = cycling(cycle, X, saves, crt)
                X += int(cmd[1])
    print(f"Part 1: {sum(saves.values())}\nPart 2:\n" + '\n'.join(crt))
