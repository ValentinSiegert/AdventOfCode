from collections import defaultdict
from heapq import heappop, heappush
from math import inf


def dijkstra(heat_map: list[list[int]], min_steps: int, max_steps: int) -> int:
    """
    This is a modified version of Dijkstra's algorithm. Instead of keeping track of the shortest distance to each node,
    we keep track of the shortest distance to each node and the direction we came from. This is because we can move in
    any direction, but we can't move back in the direction we came from. We also keep track of the number of steps we
    have taken in the current direction. If we have taken less than min_steps steps in the current direction, we can't
    move in another direction. If we have taken more than min_steps steps in the current direction, we can move in
    another direction. If we have taken more than max_steps steps in the current direction, we must move in another
    direction. We use a heap to keep track of the nodes we have visited, and we only visit a node if we can move in
    this node's direction. We also keep track of the shortest distance to each node, and we only visit a node if we
    have found a shorter path to this node. If we have visited all nodes, we return the shortest distance to the
    bottom-right node. If we have visited all nodes, and we haven't found a path to the bottom-right node, we return -1.
    :param heat_map: The heat map aka the grid.
    :param min_steps: The minimum number of steps we must take in the current direction before we can move in another.
    :param max_steps: The maximum number of steps we can take in the current direction before we must move in another.
    :return: The shortest distance to the bottom-right node or -1 if we can't reach the bottom-right node.
    """
    y_len, x_len = len(heat_map), len(heat_map[0])
    distances = defaultdict(lambda: inf)
    heap = [(0, (0, 0, (0, 1))), (0, (0, 0, (1, 0)))]
    while heap:
        cost, (y, x, directions) = heappop(heap)
        if (y, x) == (y_len - 1, x_len - 1):
            return cost
        if cost > distances[y, x, directions]:
            continue
        dir_y, dir_x = directions
        for new_dir_y, new_dir_x in ((-dir_x, dir_y), (dir_x, -dir_y)):
            new_cost = cost
            for dist in range(1, max_steps + 1):
                new_y, new_x = y + new_dir_y * dist, x + new_dir_x * dist
                if 0 <= new_y < y_len and 0 <= new_x < x_len:
                    new_cost += heat_map[new_y][new_x]
                    if dist < min_steps:
                        continue
                    new_node_and_diffs = (new_y, new_x, (new_dir_y, new_dir_x))
                    if new_cost < distances[new_node_and_diffs]:
                        distances[new_node_and_diffs] = new_cost
                        heappush(heap, (new_cost, new_node_and_diffs))
    return -1


if __name__ == '__main__':
    with open('day17.txt') as log_file:
        hm = [[int(l) for l in line] for line in log_file.read().splitlines()]
    print(f'Least heat loss for crucible: {dijkstra(hm, 1, 3)}')
    print(f'Least heat loss for ultra crucible: {dijkstra(hm, 4, 10)}')
