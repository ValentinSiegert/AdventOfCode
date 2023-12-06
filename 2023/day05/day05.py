if __name__ == '__main__':
    numbers, ranges, map_ranges, mapped_r = [], [], [], []
    with open('day05.txt') as log_file:
        for line in log_file:
            if line.strip() == '':
                map_ranges += [r for i_r, r in enumerate(ranges) if i_r not in mapped_r]
                ranges = map_ranges if map_ranges else ranges
                in_map, mapped, map_ranges, mapped_r = False, [], [], []
            elif line.strip().endswith('map:'):
                in_map = True
            elif line.strip().startswith('seeds:'):
                numbers = [int(num) for num in line.strip().split(':')[1].strip().split()]
                ranges = [range(s, s + l) for s, l in zip(numbers[0::2], numbers[1::2])]
            elif in_map:
                dest, src, length = map(int, line.strip().split())
                for i, n in enumerate(numbers):
                    if src <= n <= src + length - 1 and i not in mapped:
                        numbers[i] = dest + (n - src)
                        mapped.append(i)
                map_range, offset_start = range(src, src + length), dest + (r.start - map_range.start)
                for i_r, r in enumerate(ranges):
                    if i_r not in mapped_r:
                        if map_range.start <= r.start and r.stop <= map_range.stop:
                            map_ranges.append(range(offset_start, offset_start + (r.stop - r.start)))
                            mapped_r.append(i_r)
                        elif map_range.start <= r.start <= map_range.stop < r.stop:
                            new_r = range(offset_start, offset_start + (map_range.stop - r.start))
                            map_ranges.append(new_r)
                            ranges[i_r] = range(r.start + len(new_r), r.stop)
                        elif r.start < map_range.start <= r.stop <= map_range.stop:
                            new_r = range(dest, dest + (r.stop - map_range.start))
                            map_ranges.append(new_r)
                            ranges[i_r] = range(r.start, r.start + len(r) - len(new_r))
    print(f'The lowest location number is: {min(numbers)}')
    print(f'The lowest location number based on ranges is: {min([r.start for r in ranges])}')
