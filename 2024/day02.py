def valid_pair(pair: tuple[int, int], direction: str) -> str:
    if 1 <= abs(pair[0] - pair[1]) <= 3:
        if pair[0] < pair[1]:
            if direction == "" or direction == "inc":
                return "inc"
            elif direction == "dec":
                return ""
        elif pair[0] > pair[1]:
            if direction == "" or direction == "dec":
                return "dec"
            elif direction == "inc":
                return ""
    return ""

def validate_reports(data: str, skip_one : bool = False) -> int:
    reports = [list(map(int, line.split())) for line in data.splitlines()]
    cr = 0
    # validity = []
    valid_reports = 0
    for report in reports:
        direction, is_valid_report, skip_one_in_report, idx, fork_idx, fork_dir, skip_first = "", False, skip_one, 0, -1, "", ""
        while idx < len(report):
            if idx == len(report) - 1:
                is_valid_report = True
                break
            last_direction = direction
            direction = valid_pair((report[idx], report[idx + 1]), direction)
            if not direction:
                if skip_one_in_report:
                    skip_right = valid_pair((report[idx], report[idx + 2]), last_direction) if idx + 2 < len(report) else "True"
                    skip_left = valid_pair((report[idx - 1], report[idx + 1]), last_direction) if idx > 0 else "True"
                    if idx == 1:
                        skip_first = valid_pair((report[idx], report[idx + 1]), skip_first)
                    if skip_first and skip_left and skip_right:
                        fork_idx = idx
                        fork_dir = (skip_right, skip_first)
                        idx += 1
                        direction = skip_left
                    elif skip_first and skip_left:
                        fork_idx = idx
                        fork_dir = skip_first
                        idx += 1
                        direction = skip_left
                    elif skip_first and skip_right:
                        fork_idx = idx
                        fork_dir = skip_first
                        idx += 2
                        direction = skip_right
                    elif skip_left and skip_right:
                        fork_idx = idx
                        fork_dir = skip_right
                        idx += 1
                        direction = skip_left if skip_left != "True" else ""
                    elif skip_left:
                        idx += 1
                        direction = skip_left if skip_left != "True" else ""
                    elif skip_right:
                        if skip_right == "True":
                            is_valid_report = True
                            break
                        idx += 2
                        direction = skip_right
                    else:
                        break
                    skip_one_in_report = False
                elif fork_idx > -1:
                    if type(fork_dir) == tuple:
                        if fork_dir[0] == "True":
                            is_valid_report = True
                            break
                        direction = fork_dir[0]
                        idx = fork_idx + 2
                        fork_dir = fork_dir[1]
                    else:
                        if fork_dir == "True":
                            is_valid_report = True
                            break
                        direction = fork_dir
                        idx = fork_idx + 2 if not skip_first else fork_idx + 1
                        fork_idx = -1
                else:
                    break
            else:
                idx += 1
        # for idx, level in enumerate(report):
        #     if idx == len(report) - 1:
        #         is_valid_report = True
        #     elif 1 <= abs(level - report[idx + 1]) <= 3:
        #         if level < report[idx + 1]:
        #             if direction == "":
        #                 direction = "inc"
        #             elif direction == "dec":
        #                 break
        #         elif level > report[idx + 1]:
        #             if direction == "":
        #                 direction = "dec"
        #             elif direction == "inc":
        #                 break
        #     else:
        #         break
        cr += 1
        valid_reports += int(is_valid_report)
        # validity.append(is_valid_report)
        # print(f"{' '.join([str(r) for r in report])}\t\t{is_valid_report}")
        # print(f"{' '.join([str(r) for r in report])}") if is_valid_report and not skip_one_in_report else None
        print(f"{' '.join([str(r) for r in report])}") if not is_valid_report else None
    return valid_reports


def part1(data : str) -> int:
    return validate_reports(data)

def part2(data : str) -> int:
    return validate_reports(data, True)

def solve(data, part):
    def is_safe(row):
        inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
        if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
            return True
        return False

    data = [[int(y) for y in x.split(' ')] for x in data.splitlines()]

    safe_count = sum([is_safe(row) for row in data])
    print(safe_count)

    safe_count = sum([any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in data])
    print(safe_count)
    if part == 1:
        return part1(data)
    if part == 2:
        r = part2(data)
        print(r)
        return r
    responses = [part1(data), part2(data)]
    # validity1 = responses[0][1]
    # validity2 = responses[1][1]
    # for idx, (v1, v2) in enumerate(zip(validity1, validity2)):
    #     if v1 != v2:
    #         print(f"idx: {idx}, v1: {v1}, v2: {v2}")
    return responses
