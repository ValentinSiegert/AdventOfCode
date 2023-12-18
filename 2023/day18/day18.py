if __name__ == '__main__':
    next_dir = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}
    with open('day18.txt') as log_file:
        lagoon, boundaries, real_lagoon, real_boundaries = [], 0, [], 0
        for line in log_file:
            direc, steps, color = line.split()
            steps, color = int(steps), color.replace('(', '').replace(')', '').replace('#', '')
            last, boundaries = lagoon[-1] if lagoon else (0, 0), boundaries + steps
            lagoon.append((last[0] + steps * next_dir[direc][0], last[1] + steps * next_dir[direc][1]))
            real_dir = 'R' if color[-1] == '0' else 'D' if color[-1] == '1' else 'L' if color[-1] == '2' else 'U'
            real_steps = int(color[:-1], 16)
            real_last, real_boundaries = real_lagoon[-1] if real_lagoon else (0, 0), real_boundaries + real_steps
            real_lagoon.append((real_last[0] + real_steps * next_dir[real_dir][0],
                                real_last[1] + real_steps * next_dir[real_dir][1]))
    # Shoelace formula https://en.wikipedia.org/wiki/Shoelace_formula#Triangle_formula
    area = lambda points: abs(sum(p1[0] * p2[1] - p1[1] * p2[0] for p1, p2 in zip(points[:-1], points[1:]))) // 2
    # Based on Pick's theorem https://en.wikipedia.org/wiki/Pick%27s_theorem
    # A = i + b/2 - 1   i: number interior points  b: number of boundary points
    # i = A - b/2 + 1
    # i + b = A + b/2 + 1
    print(f'Lagoon can hold cubic meters of lava: {area(lagoon) + boundaries // 2 + 1}')
    print(f'Real lagoon can hold cubic meters of lava: {area(real_lagoon) + real_boundaries // 2 + 1}')
