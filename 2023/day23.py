if __name__ == '__main__':
    with open('day23.txt') as log_file:
        hiking_map = [line.strip() for line in log_file]
    start, end = (hiking_map[0].find('.'), 0), (hiking_map[-1].find('.'), y_max := len(hiking_map) - 1)
    q, x_max, paths = [(start[0], start[1], start[0], -1, 0)], len(hiking_map[0]) - 1, []
    while q:
        x, y, xb, yb, steps = q.pop(0)
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x1, y1 = x + i, y + j
            if (x1, y1) == (xb, yb):
                continue
            if (x1, y1) == end:
                paths.append(steps + 1)
                break
            if 0 <= x1 <= x_max and 0 <= y1 <= y_max and ((hmp := hiking_map[y1][x1]) == '.' or (hmp == 'v' and j == 1)
                                                          or (hmp == '^' and j == -1) or (hmp == '>' and i == 1)
                                                          or (hmp == '<' and i == -1)):
                new_steps = steps + 2 if hmp in 'v<>' else steps + 1
                x1 += 1 if hmp == '>' else -1 if hmp == '<' else 0
                y1 += 1 if hmp == 'v' else -1 if hmp == '^' else 0
                q.append((x1, y1, x, y, new_steps))
    print(f'The longest hike with icy slopes is: {max(paths)}')
    graph = {start: {}, end: {}}
    for y, line in enumerate(hiking_map):
        for x, char in enumerate(line):
            if hiking_map[y][x] != '#':
                neighbors = len([1 for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)] if 0 <= x + i <= x_max and
                                 0 <= y + j <= y_max and hiking_map[y + j][x + i] != '#'])
                if neighbors > 2:
                    graph[(x, y)] = {}
    for node in graph:
        q = [(node[0], node[1], node[0], node[1], 0)]
        while q:
            x, y, xb, yb, steps = q.pop(0)
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x1, y1 = x + i, y + j
                if (x1, y1) == (xb, yb):
                    continue
                if (x1, y1) in graph and (x1, y1) != node:
                    graph[node][(x1, y1)] = steps + 1
                    break
                if 0 <= x1 <= x_max and 0 <= y1 <= y_max and hiking_map[y1][x1] != '#':
                    q.append((x1, y1, x, y, steps + 1))
    q, max_steps, visited = [(start, 0)], 0, set()
    while q:
        node, steps = q.pop()
        if steps == -1:
            visited.remove(node)
            continue
        if node == end:
            max_steps = max(max_steps, steps)
            continue
        if node in visited:
            continue
        visited.add(node)
        q.append((node, -1))
        for neighbor in graph[node].keys():
            q.append((neighbor, steps + graph[node][neighbor]))
    print(f'The longest hike without easy slopes is: {max_steps}')
    
