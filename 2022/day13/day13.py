import json
from functools import cmp_to_key


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return 0 if a == b else -1 if a < b else 1
    elif isinstance(a, list) or isinstance(b, list):
        result = 0
        a = [a] if not isinstance(a, list) else a
        b = [b] if not isinstance(b, list) else b
        for a_, b_ in zip(a, b):
            result = compare(a_, b_)
            if result != 0:
                return result
        if result == 0 and len(a) != len(b):
            return -1 if len(a) < len(b) else 1
        return result


if __name__ == '__main__':
    data = list(map(lambda x: [json.loads(y) for y in x.split('\n')], open('day13.txt').read().split('\n\n')))
    correct = 0
    for group_index, group in enumerate(data, 1):
        correct += group_index if compare(group[0], group[1]) == -1 else 0
    data = [part for group in data for part in group] + [[[2]], [[6]]]
    data.sort(key=cmp_to_key(compare))
    print(f"Part 1: {correct}")
    print(f"Part 2: {(data.index([[2]]) + 1) * (data.index([[6]]) + 1)}")
