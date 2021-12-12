
PART2 = True


def check_single_cave_twice(path):
    check = []
    check2 = []
    for p in [pt for pt in path if pt.islower()]:
        if p not in check:
            check.append(p)
        else:
            check2.append(p)
    return len(check2) > 0


def find_all_paths(graph, start, end, path=None):
    if not path:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if (node.islower() and node not in path) or node.isupper() or \
                (PART2 and node.islower() and node not in ['start', 'end'] and not check_single_cave_twice(path)):
            new_paths = find_all_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


if __name__ == '__main__':
    cave_graph = {}
    with open('day12.txt') as logfile:
        for line in logfile:
            a, b = line.strip().split('-')
            if a not in cave_graph.keys():
                cave_graph[a] = [b]
            else:
                cave_graph[a].append(b)
            if b not in cave_graph.keys():
                cave_graph[b] = [a]
            else:
                cave_graph[b].append(a)
    all_paths = find_all_paths(cave_graph, 'start', 'end')
    print(f'Paths through this cave system that visit small caves at most once: {len(all_paths)}')
