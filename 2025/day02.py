import re


def invalid_id_detector(data: str, p2: bool = False) -> int:
    id_ranges = list(map(lambda x: tuple(map(int, x.split('-'))), data.replace('\n', '').split(',')))
    all_ids, invalid_ids = [i for start, end in id_ranges for i in range(start, end + 1)], []
    if not p2:
        return sum([id_c for id_c in all_ids if (id_len:=len(id_s:=str(id_c))) % 2 == 0 and
                    id_s[:id_len//2] == id_s[id_len//2:]])
    else:
        return sum(map(int, [m.group(0) for m in re.finditer(r'^(\d+)\1+$', '\n'.join(map(str, all_ids)),
                                                             flags=re.MULTILINE)]))


def solve(data: str, part: int) -> int | tuple[int, int]:
    if part == 1:
        return invalid_id_detector(data)
    if part == 2:
        return invalid_id_detector(data, True)
    return invalid_id_detector(data), invalid_id_detector(data, True)
