BRUTEFORCE = False

def valid_report(report: list[int]) -> bool:
    directions = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    return True if set(directions) <= {1, 2, 3} or set(directions) <= {-1, -2, -3} else False


def brute_force(data: str, skip_one: bool = False) -> int:
    reports = [[int(y) for y in x.split(' ')] for x in data.splitlines()]
    if not skip_one:
        return sum([valid_report(report) for report in reports])
    else:
        return sum([any([valid_report(report[:i] + report[i + 1:]) for i in range(len(report))]) for report in reports])


def valid_pair(pair: tuple[int, int], direction: str) -> str:
    if 1 <= abs(pair[0] - pair[1]) <= 3:
        if pair[0] < pair[1]:
            return "+" if direction == "" or direction == "+" else ""
        elif pair[0] > pair[1]:
            return "-" if direction == "" or direction == "-" else ""
    return ""

def validate_reports(data: str, skip_one : bool = False) -> int:
    reports = [list(map(int, line.split())) for line in data.splitlines()]
    valid_reports = 0
    for report in reports:
        direction, is_valid_report, skip_one_in_report, idx, skips = "", False, skip_one, 0, []
        while idx < len(report):
            if idx == len(report) - 1:
                is_valid_report = True
                break
            last_direction = direction
            if not (direction := valid_pair((report[idx], report[idx + 1]), direction)):
                if skip_one_in_report:
                    if idx + 2 >= len(report):
                        is_valid_report = True
                        break
                    skips.append((skip_left, idx, 1)) if (skip_left := valid_pair((report[idx - 1], report[idx + 1]), last_direction) if idx > 0 else "empty") else None
                    skips.append((skip_right, idx, 2)) if (skip_right := valid_pair((report[idx], report[idx + 2]), last_direction)) else None
                    skips.append((skip_first, idx, 1)) if (skip_first := valid_pair((report[1], report[2]), '')) and idx == 1 else None
                    skips.append((skip_second, idx, 1)) if (skip_second := valid_pair((report[0], report[2]), '')) and idx == 1 else None
                    skip_one_in_report = False
                if skips:
                    next_skip = skips.pop(0)
                    direction = '' if next_skip[0] == "empty" else next_skip[0]
                    idx = next_skip[1] + next_skip[2]
                else:
                    break
            else:
                idx += 1
        valid_reports += int(is_valid_report)
    return valid_reports


def part1(data : str) -> int:
    if BRUTEFORCE:
        return brute_force(data)
    return validate_reports(data)

def part2(data : str) -> int:
    if BRUTEFORCE:
        return brute_force(data, True)
    return validate_reports(data, True)

def solve(data, part):
    if part == 1:
        return part1(data)
    if part == 2:
        return part2(data)
    return [part1(data), part2(data)]
