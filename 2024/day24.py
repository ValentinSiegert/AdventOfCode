import re


def part1(wires: dict[str, int], gates: list[tuple[str, str, str, str]]) -> int:
    """
    Simulates the circuit to calculate the integer all z wires concatenated in reverse order represent.
    :param wires: the dictionary of initial wires with their values.
    :param gates: the list of gates with their operands and results in wire format.
    :return: the integer all z wires concatenated in reverse order represent.
    """
    while len(gates):
        a, op, b, res = gates.pop(0)
        if (op1 := wires.get(a, None)) is not None and (op2 := wires.get(b, None)) is not None:
            wires[res] = op1 & op2 if op == 'AND' else op1 | op2 if op == 'OR' else op1 ^ op2
        else:
            gates.append((a, op, b, res))
    return int(''.join([f'{wires[z]}' for z in sorted([k for k in wires if k.startswith('z')], reverse=True)]), 2)


def part2(gates: list[tuple[str, str, str, str]]) -> str:
    """
    Find all wrong resulting wires in the circuit and return them in alphabetical order. We assume that the circuit
    should represent an x-bit adder consisting of one half adder and x-1 full adders.
    :param gates: the list of gates with their operands and results in wire format.
    :return: all wrong resulting wires in the circuit in alphabetical order separated by commas.
    """
    wrong, z_max = set(), f'z{max([int(z[1:]) for _, _, _, z in gates if z.startswith("z")])}'
    for a, op, b, res in gates:
        """
        The following conditions are checked by line:
        1. If the result is a z-wire and is not the maximum z wire there should be an XOR operation performed.
        2. If the operation is XOR, one of the two inputs and the output requires to be an x-, y- or z-wire.
        3. If the operation is AND and it is not the half adder of x0 and y0, the result requires to be part of an OR operation.
        4. If the operation is XOR, the result requires to be part of an AND operation.
        """
        if ((res.startswith('z') and op != "XOR" and res != z_max) or
            (op == "XOR" and res[0] not in 'xyz' and a[0] not in 'xyz' and b[0] not in 'xyz') or
            (op == "AND" and "x00" not in [a, b] and any(((res == i1 or res == i2) and x != "OR") for i1, x, i2, r in gates)) or
            (op == "XOR" and any(((res == i1 or res == i2) and x != "AND") for i1, x, i2, r in gates))):
            wrong.add(res)
    return ','.join(sorted(wrong))


def solve(data: str, part: int):
    (inits, gates) = data.split('\n\n')
    wires = {k: int(v) for k, v in re.findall(r'(\w+): (\w+)', inits)}
    gates = [(a, op, b, res) for a, op, b, res in re.findall(r'(\w{3})\s(AND|OR|XOR)\s(\w{3})\s->\s(\w{3})', gates)]
    if part == 1: return part1(wires, gates)
    if part == 2: return part2(gates)
    return [part1(wires, gates.copy()), part2(gates)]
