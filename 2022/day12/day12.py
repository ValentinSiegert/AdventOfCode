def hiking(part):
    mapl = list(map(list, open("day12.txt").read().splitlines()))
    end = (0, 0)
    starts = []
    for y, r in enumerate(mapl):
        for x, c in enumerate(r):
            match c:
                case "S":
                    starts.append((x, y))
                    c = (ord('a'), 0)
                case "E":
                    end = (x, y)
                    c = (ord('z'), None)
                case _:
                    if c == 'a' and part == 2:
                        starts.append((x, y))
                        c = (ord('a'), 0)
                    else:
                        c = (ord(c), None)
            mapl[y][x] = c
    found, nodes = False, starts
    while not found:
        new_nodes = []
        for n in nodes:
            if n == end:
                found = True
                break
            if n[0] > 0 and mapl[n[1]][n[0] - 1][1] is None and mapl[n[1]][n[0] - 1][0] <= mapl[n[1]][n[0]][0] + 1:
                new_nodes.append((n[0] - 1, n[1]))
                mapl[n[1]][n[0] - 1] = (mapl[n[1]][n[0] - 1][0], mapl[n[1]][n[0]][1] + 1)
            if n[0] < len(mapl[0]) - 1 and mapl[n[1]][n[0] + 1][1] is None and \
                    mapl[n[1]][n[0] + 1][0] <= mapl[n[1]][n[0]][0] + 1:
                new_nodes.append((n[0] + 1, n[1]))
                mapl[n[1]][n[0] + 1] = (mapl[n[1]][n[0] + 1][0], mapl[n[1]][n[0]][1] + 1)
            if n[1] > 0 and mapl[n[1] - 1][n[0]][1] is None and mapl[n[1] - 1][n[0]][0] <= mapl[n[1]][n[0]][0] + 1:
                new_nodes.append((n[0], n[1] - 1))
                mapl[n[1] - 1][n[0]] = (mapl[n[1] - 1][n[0]][0], mapl[n[1]][n[0]][1] + 1)
            if n[1] < len(mapl) - 1 and mapl[n[1] + 1][n[0]][1] is None and \
                    mapl[n[1] + 1][n[0]][0] <= mapl[n[1]][n[0]][0] + 1:
                new_nodes.append((n[0], n[1] + 1))
                mapl[n[1] + 1][n[0]] = (mapl[n[1] + 1][n[0]][0], mapl[n[1]][n[0]][1] + 1)
        nodes = new_nodes
    return mapl[end[1]][end[0]][1]


if __name__ == "__main__":
    print(f"Part 1: {hiking(1)}\nPart 2: {hiking(2)}")
