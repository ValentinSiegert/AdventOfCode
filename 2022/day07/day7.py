import re, pathlib


def size(dic, m):
    for key in [k for k, v in dic.items() if k != '_s' and v['_s'] == 0]:
        dic[key]['_s'], m = size(dic[key], m)
    m += res if (res := sum([v['_s'] for k, v in dic.items() if k != '_s'])) <= 100000 else 0
    return res, m


def best_del(dic, best, req):
    best = dic['_s'] if req <= dic['_s'] <= best else best
    for key in [k for k, v in dic.items() if k != '_s' and len(v.keys()) > 1]:
        best = new_best if req <= (new_best := best_del(dic[key], best, req)) <= best else best
    return best


if __name__ == "__main__":
    sys, breadcrumbs = {'\\': {'_s': 0}}, pathlib.Path('\\')
    with open("day7.txt") as f:
        for line in f:
            curr_dir = sys
            for bc in breadcrumbs.parts:
                curr_dir = curr_dir[bc]
            if cm := re.match(r"\$\scd\s(?P<dir>[a-z.]+)", line):
                if cm.group("dir") == '..':
                    breadcrumbs = breadcrumbs.parent
                else:
                    if cm.group("dir") not in curr_dir:
                        curr_dir[cm.group("dir")] = {'_s': 0}
                    breadcrumbs /= cm.group("dir")
            elif dt := re.match(r"(?P<size>\d+)\s(?P<name>[a-z.]+)", line):
                curr_dir[dt.group("name")] = {'_s': int(dt.group("size"))}
    sys['\\']['_s'], minors = size(sys['\\'], 0)
    print(f"Part 1: {minors}")
    print("Part 2:", best_del(sys['\\'], sys['\\']['_s'], 30000000 - (70000000 - sys['\\']['_s'])))
