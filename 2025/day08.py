import heapq
from itertools import combinations
from math import prod


def jboxes(data: str, p2: bool = False) -> int:
    points = list(map(lambda d: tuple(map(int,d.split(','))), data.splitlines()))
    pairs = [(p, q, sum((a - b) ** 2 for a, b in zip(p, q))) for p, q in combinations(points, 2)]
    pairs = heapq.nsmallest((len(pairs) if p2 else 1000), pairs, key=lambda x: x[2])
    circuits = {p: i for i, p in enumerate(points)}
    for i in range(len(pairs)):
        if (c1:=circuits[(pair:=pairs[i])[0]]) == (c2:=circuits[pair[1]]):
            continue
        for c in circuits:
            circuits[c] = c1 if circuits[c] == c2 else circuits[c]
        if len(set(circuits.values())) == 1:
            break
    return pair[0][0] * pair[1][0] if p2 else prod(sorted([len([p for p in circuits.values() if p == c]) for c in set(circuits.values())], reverse=True)[:3])


def solve(data: str, part: int) -> int | tuple[int, int]:
    if part == 1:
        return jboxes(data)
    if part == 2:
        return jboxes(data, True)
    return jboxes(data), jboxes(data, True)
