import copy


def calc_lowest_risk(risk_levels, downs=None, rights=None):
    for y in range(len(risk_levels) - 1, -1, -1):
        for x in range(len(risk_levels[0]) - 1, -1, -1):
            if not downs:
                down = risk_levels[y + 1][x] if y + 1 < len(risk_levels) else None
            else:
                down = risk_levels[y + 1][x] if y + 1 < len(risk_levels) else downs[x]
            if not rights:
                right = risk_levels[y][x + 1] if x + 1 < len(risk_levels[0]) else None
            else:
                right = risk_levels[y][x + 1] if x + 1 < len(risk_levels[0]) else rights[y]
            if down and right:
                risk_levels[y][x] += min(down, right)
            elif down:
                risk_levels[y][x] += down
            elif right:
                risk_levels[y][x] += right
    return risk_levels


def calc_lowest_risk_ext(risk_levels):
    grid = [[[j, [], []] for j in range(i, i + 5)] for i in range(0, 5)]
    for l in range(len(grid) - 1, -1, -1):
        for c in range(len(grid[0]) - 1, -1, -1):
            temp_risks = [[j + grid[l][c][0] if j + grid[l][c][0] < 10 else (j + grid[l][c][0]) % 9 for j in i]
                          for i in risk_levels]
            temp_downs = grid[l + 1][c][1] if l + 1 < len(grid) else None
            temp_rights = grid[l][c + 1][2] if c + 1 < len(grid[0]) else None
            t_debug = copy.deepcopy(temp_risks)
            temp_risks = calc_lowest_risk(temp_risks, temp_downs, temp_rights)
            grid[l][c][1] = temp_risks[0]
            grid[l][c][2] = [t[0] for t in temp_risks]
    return temp_risks


def calc_lowest_risk_ext2(risk_levels):
    grid = [[j for j in range(i, i + 5)] for i in range(0, 5)]
    global_risks = []
    for l1 in range(len(grid)):
        for c1 in range(len(grid[0])):
            temp_risks = [[j + grid[l1][c1] if j + grid[l1][c1] < 10 else (j + grid[l1][c1]) % 9 for j in i]
                          for i in risk_levels]
            grid[l1][c1] = temp_risks
    for l2 in range(len(grid)):
        for y1 in range(len(risk_levels)):
            global_risks.append(grid[l2][0][y1] + grid[l2][1][y1] + grid[l2][2][y1] + grid[l2][3][y1] + grid[l2][4][y1])
    g_debug = copy.deepcopy(global_risks)
    global_risks = calc_lowest_risk(global_risks)
    return global_risks


if __name__ == '__main__':
    risks = [[i for i in map(int, line.strip())] for line in open('day15.txt').readlines()]
    risks1 = copy.deepcopy(risks)
    risks1 = calc_lowest_risk(risks1)
    print(f'Lowest Risk in part 1: {min(risks1[0][1], risks1[1][0])}')
    risks2 = copy.deepcopy(risks)
    risks2 = calc_lowest_risk_ext(risks2)
    print(f'Lowest Risk in part 2: {min(risks2[0][1], risks2[1][0])}')
    risks3 = copy.deepcopy(risks)
    risks3 = calc_lowest_risk_ext2(risks3)
    print(f'Lowest Risk in part 2: {min(risks3[0][1], risks3[1][0])}')
