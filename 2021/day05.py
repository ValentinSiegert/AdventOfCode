

if __name__ == '__main__':
    only_part1 = False
    vents = {}
    with open('day5.txt') as logfile:
        for line in logfile:
            borders = line.strip().split(' -> ')
            start = list(map(int, borders[0].split(',')))
            end = list(map(int, borders[1].split(',')))
            if start[0] == end[0] or start[1] == end[1]:  # the horizontal and vertical lines
                if start[0] == end[0]:
                    x1 = x2 = start[0]
                    y1 = start[1] if start[1] < end[1] else end[1]
                    y2 = start[1] if start[1] > end[1] else end[1]
                elif start[1] == end[1]:
                    y1 = y2 = start[1]
                    x1 = start[0] if start[0] < end[0] else end[0]
                    x2 = start[0] if start[0] > end[0] else end[0]
                line_points = [(x, y) for y in range(y1, y2+1) for x in range(x1, x2+1)]
            else:  # found diagonal line
                if only_part1:
                    continue
                if start[0] < end[0]:
                    x1 = start[0]
                    x2 = end[0]
                    y1 = start[1]
                    y2 = end[1]
                elif start[0] > end[0]:
                    x1 = end[0]
                    x2 = start[0]
                    y1 = end[1]
                    y2 = start[1]
                if (start[0] < end[0] and start[1] < end[1]) or (start[0] > end[0] and start[1] > end[1]):
                    line_points = [(x, y1+(x-x1)) for x in range(x1, x2+1)]
                else:
                    line_points = [(x, y1-(x-x1)) for x in range(x1, x2+1)]
            for x, y in line_points:
                if (x, y) in vents.keys():
                    vents[(x, y)] += 1
                else:
                    vents[(x, y)] = 1
    overlaps = {key: value for key, value in vents.items() if value > 1}
    print(f'The amount of overlapping horizontal and vertical lines is {len(overlaps.keys())}.')
