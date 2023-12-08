import itertools
from math import gcd

if __name__ == '__main__':
    with open('day08.txt') as log_file:
        instructions, graph = log_file.read().split('\n\n')
    graph = {(key_vals := line.replace(')', '').split(' = ('))[0]: [v.strip() for v in key_vals[1].split(',')] for line in graph.splitlines()}
    instruction_iterator = itertools.cycle(instructions)
    node, steps = 'AAA', 0
    while node != 'ZZZ':
        instruction = next(instruction_iterator)
        steps += 1
        if instruction == 'L':
            node = graph[node][0]
        elif instruction == 'R':
            node = graph[node][1]
    print(f"There are {steps} steps required to get from 'AAA' to 'ZZZ'.")
    nodes = [n for n in graph.keys() if n.endswith('A')]
    ghost_steps = [0 for _ in range(len(nodes))]
    for idx, node in enumerate(nodes):
        instruction_iterator = itertools.cycle(instructions)
        while not node.endswith('Z'):
            instruction = next(instruction_iterator)
            ghost_steps[idx] += 1
            if instruction == 'L':
                node = graph[node][0]
            elif instruction == 'R':
                node = graph[node][1]
    ghost_lcm = 1
    for ghost_step in ghost_steps:
        ghost_lcm = ghost_lcm * ghost_step // gcd(ghost_lcm, ghost_step)
    print(f"There are {ghost_lcm} ghost steps required to get from all A nodes to Z nodes.")
