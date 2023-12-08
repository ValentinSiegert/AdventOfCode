import itertools
from math import gcd


def iter_graph(instruction_iterator: itertools.cycle, node: str, z_ending: bool = False) -> int:
    """
    Iterates through the graph until it reaches a node that ends with 'Z' or 'ZZZ' and returns the number of steps.
    :param instruction_iterator: The iterator that will be used to iterate through the instructions.
    :param node: The node to start at.
    :param z_ending: Whether to end at a node that ends with 'Z' or 'ZZZ'.
    :return: The number of steps it took to reach the final node.
    """
    steps = 0
    while (lambda n: n != 'ZZZ' if not z_ending else not n.endswith('Z'))(node):
        instruction = next(instruction_iterator)
        steps += 1
        if instruction == 'L':
            node = graph[node][0]
        elif instruction == 'R':
            node = graph[node][1]
    return steps


if __name__ == '__main__':
    with open('day08.txt') as log_file:
        instructions, graph = log_file.read().split('\n\n')
    graph = {(key_vals := line.replace(')', '').split(' = ('))[0]: [v.strip() for v in key_vals[1].split(',')] for line
             in graph.splitlines()}
    print(f"There are {iter_graph(itertools.cycle(instructions), 'AAA')} steps required to get from 'AAA' to 'ZZZ'.")
    nodes = [n for n in graph.keys() if n.endswith('A')]
    ghost_steps = [iter_graph(itertools.cycle(instructions), n, True) for n in nodes]
    ghost_lcm = 1
    for ghost_step in ghost_steps:
        ghost_lcm = ghost_lcm * ghost_step // gcd(ghost_lcm, ghost_step)
    print(f"There are {ghost_lcm} ghost steps required to get from all A nodes to Z nodes.")
