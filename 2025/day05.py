
def part2(freshs: list[range], i: int = 0) -> int:
    freshs.sort(key=lambda r: r.start)
    while i < len(freshs) - 1:
        if freshs[i].stop >= freshs[i + 1].start:
            freshs[i] = range(freshs[i].start, max(freshs[i].stop, freshs[i + 1].stop))
            del freshs[i + 1]
        else:
            i += 1
    return sum(map(lambda r: len(r), freshs))


def solve(data: str, part: int) -> int | tuple[int, int]:
    freshs, availables = (list(map(lambda r: range(int((rs := r.split('-'))[0]), int(rs[1]) + 1),
                                   (splits := data.split('\n\n'))[0].splitlines())),
                          list(map(int, splits[1].splitlines())))
    if part == 1:
        return sum(map(lambda a: any(map(lambda r: int(a) in r, freshs)), availables))
    if part == 2:
        return part2(freshs)
    return sum(map(lambda a: any(map(lambda r: int(a) in r, freshs)), availables)), part2(freshs)
