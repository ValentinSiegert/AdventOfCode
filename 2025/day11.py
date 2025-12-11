from functools import cache
from math import prod


def start_end_traverse(data: str) -> int:
    graph = {nodes[0][:-1]: nodes[1:] for nodes in (line.split() for line in data.splitlines())}
    paths, path_amount = [['you']], 0
    while path := paths.pop() if paths else None:
        for neighbor in graph[path[-1]]:
            if neighbor == 'out':
                path_amount += 1
            elif neighbor not in path:
                paths.append(path + [neighbor])
    return path_amount


def traverse(data: str, parts: int = 0) -> int | tuple[int, int]:
    graph = {nodes[0][:-1]: set(nodes[1:]) for nodes in (line.split() for line in data.splitlines())}
    @cache
    def visit(current: str, destination: str) -> int:
        return 1 if current == destination else sum(visit(node, destination) for node in graph.get(current, set()))
    def traverse_requires(requires: list[list[str]], path_amount: int = 0) -> int:
        for required in requires:
            path_amount += prod(visit(required[i], required[i + 1]) for i in range(len(required) - 1))
        return path_amount
    if parts == 1:
        return traverse_requires([['you', 'out']])
    elif parts == 2:
        return traverse_requires([['svr', 'fft', 'dac', 'out'], ['svr', 'dac', 'fft', 'out']])
    return traverse_requires([['you', 'out']]), traverse_requires([['svr', 'fft', 'dac', 'out'], ['svr', 'dac', 'fft', 'out']])


def solve(data: str, part: int) -> int | tuple[int, int]:
    if part == 1:
        return traverse(data, 1)
    if part == 2:
        return traverse(data, 2)
    return traverse(data)