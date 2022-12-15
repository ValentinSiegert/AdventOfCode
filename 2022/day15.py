import re


def impossible_pos(row, file_name, M, part1=True):
    y_range = list(range(M + 1)) if not part1 else [row]
    for Y in y_range:
        stations, scan, sensor_dists_all, sensor_dists = set(), set(), [], []
        manhattan = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
        with open(file_name) as f:
            for line in f:
                sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
                if (dist := manhattan((sx, sy), (bx, by)) - abs(sy - Y)) >= 0:
                    sensor_dists_all.append((sx - dist, sx + dist))
                    if sy == Y:
                        stations.add(sx)
                    if by == Y:
                        stations.add(bx)
        sensor_dists_all.sort()
        for s, e in sensor_dists_all:
            if not sensor_dists:
                sensor_dists.append([s, e])
                continue
            lo, hi = sensor_dists[-1]
            if s > hi + 1:
                sensor_dists.append([s, e])
                continue
            sensor_dists[-1][1] = max(hi, e)
        if part1:
            for lo, hi in sensor_dists:
                for x in range(lo, hi + 1):
                    scan.add(x)
            return len(scan - stations)
        else:
            x = 0
            for lo, hi in sensor_dists:
                if x < lo:
                    return x * 4000000 + Y
                x = max(x, hi + 1)
                if x > M:
                    break


if __name__ == '__main__':
    print(f"Part 1 (test): {impossible_pos(10, 'day15t.txt', 0)}")
    print(f"Part 1: {impossible_pos(2000000, 'day15.txt', 0)}")
    print(f"Part 2 (test): {impossible_pos(10, 'day15t.txt', 20, False)}")
    print(f"Part 2: {impossible_pos(2000000, 'day15.txt', 4000000, False)}")
