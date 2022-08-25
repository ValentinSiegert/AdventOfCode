
def f(s, x, y):
    if s <= 0:
        return tuple([0, 0])
    else:
        result_x = 0
        if x > 0:
            i_max = s if s < x else x
            for i in range(1, i_max + 1):
                result_x += x-i+1
        elif x < 0:
            i_max = s if s <= abs(x) else x
            for i in range(1, i_max + 1):
                result_x += x+i-1
        result_y = 0
        for i in range(1, s + 1):
            result_y += y - i + 1
    return tuple([result_x, result_y])


if __name__ == '__main__':
    x_area, y_area = open('day17.txt').read().split()[2:]
    x_area = list(map(int, x_area[2:-1].split('..')))
    x_max = max(x_area)
    x_area = [i for i in range(x_area[0], x_area[1] + 1)]
    y_area = list(map(int, y_area[2:].split('..')))
    y_max = max(y_area)
    y_area = [i for i in range(y_area[0], y_area[1] + 1)]
    area = {tuple([x, y]) for x in x_area for y in y_area}
    del x_area, y_area
    y_once = y_last = False
    highest_y = y1 = 0
    while not y_once or y_last:
        xs = []
        for x1 in range(1, x_max + 1):
            points = set()
            for step in range(1, x_max + 1):
                points.add(f(step, x1, y1))
            intersects = bool(area & points)
            xs.append(intersects)
            if intersects:
                highest_y = max(highest_y, max(points, key=lambda e: e[1])[1])
        y_last = True if any(xs) else False
        y_once = True if not y_once and y_last else y_once
        if not y_once or y_last:
            y1 += 1
    best_y1 = y1 - 1
    print(f'Best y1 is {best_y1} with highest y position of {highest_y}')
