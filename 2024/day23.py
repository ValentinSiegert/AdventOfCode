
def part1(network: dict[str, list[str]]) -> int:
    """
    Finds the number of triangles in the network to later determine the number of triangles a host starts with t is in.
    :param network: the non-directed graph of connected computers given as input.
    :return: the number of triangles in the network where at least one host starts with t.
    """
    threer = set()
    for host, cons in network.items():
        for con in cons:
            for con2 in {c for c in network[con] if c != host} & {c for c in network[host] if c != con}:
                threer.add(tuple(sorted([host, con, con2])))
    return sum(1 for ts in threer if any(t.startswith('t') for t in ts))


def part2(network: dict[str, list[str]], currents, prospectives, processeds) -> set[str]:
    """
    Performs the Bron-Kerbosch algorithm for finding the maximum clique in the network representing the lan party.
    :param network: the non-directed graph of connected computers given as input.
    :param currents: the current set of computers in the clique.
    :param prospectives: the set of computers that can be added to the clique.
    :param processeds: the set of computers that have been processed.
    :return: the maximum clique in the network representing the lan party.
    """
    if not prospectives and not processeds:
        return currents
    max_clique = set()
    for v in list(prospectives):
        clique = part2(network, currents | {v}, prospectives & set(network[v]), processeds & set(network[v]))
        if len(clique) > len(max_clique): max_clique = clique
        prospectives.remove(v)
        processeds.add(v)
    return max_clique


def solve(data: str, part: int):
    network = {}
    for con in data.splitlines():
        con1, con2 = con.split("-")
        network.setdefault(con1, []).append(con2)
        network.setdefault(con2, []).append(con1)
    if part == 1: return part1(network)
    if part == 2: return ','.join(sorted(part2(network, set(), set(network.keys()), set())))
    return [part1(network), ','.join(sorted(part2(network, set(), set(network.keys()), set())))]
