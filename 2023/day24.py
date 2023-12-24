from itertools import combinations as combs
from decimal import Decimal as D, getcontext

getcontext().prec = 50


def line(p: tuple[D, D], v: tuple[D, D]) -> tuple[D, D]:
    """
    Produces gradient and constant of a line given by a 2D point and its velocity.
    :param p: the 2D point.
    :param v: The 2D velocity vector.
    :return: Tuple of gradient and constant.
    """
    m = v[1] / v[0] if v[0] != 0 else D('inf')
    c = p[1] - m * p[0]
    return m, c


def intersection(l1: tuple[D, D], l2: tuple[D, D]) -> tuple[D, D] or bool:
    """
    Produces the intersection point of two lines given by their gradient and constant.
    :param l1: Line 1.
    :param l2: Line 2.
    :return: The intersection point of the two lines or False if the lines are parallel.
    """
    if l2[0] - l1[0] != 0 and l1[0] != D('inf') and l2[0] != D('inf'):
        ix = (l1[1] - l2[1]) / (l2[0] - l1[0])
        iy = l1[0] * ix + l1[1]
        return ix.quantize(D(".1")), iy.quantize(D(".1"))
    return False


def intersection_in_past(p: tuple[D, D], v: tuple[D, D], i: tuple[D, D]) -> bool:
    """
    Produces True if the intersection point of two lines given by their 2D points and velocities is in the past for 
    the given point and its velocity.
    :param p: The 2D point.
    :param v: The 2D velocity.
    :param i: The intersection point of the two lines.
    :return: True if the intersection point of the two lines is in the past, False otherwise.
    """
    return ((float(p[0]) < i[0] if v[0] < 0 else float(p[0]) > i[0]) or
            (float(p[1]) < i[1] if v[1] < 0 else float(p[1]) > i[1]))


def getZ(p1: tuple[D, D, D], p1v: tuple[D, D, D], p2: tuple[D, D, D], p2v: tuple[D, D, D],
         intersec: tuple[D, D]) -> D or None:
    """
    Produces the z value of the intersection point of two lines given by their 3D points and velocities.
    :param p1: The 3D point of the first line.
    :param p1v: The 3D velocity of the first line.
    :param p2: The 3D point of the second line.
    :param p2v: The 3D velocity of the second line.
    :param intersec: The intersection point of the two lines.
    :return: The z value of the intersection point of the two lines or None if the intersection point is in the past.
    """
    # given an intersection point and an other Hail
    # now we KNOW: z = pz_i + t_i*(vz_i-aZ)   [t = (inter[0]-px_i)/(vx_i)]
    #              z = pz_j + t_j*(vz_j-aZ)
    # (pz_i - pz_j + t_i*vz_i - t_j*vz_j)/(t_i - t_j) =  aZ
    p1t = (intersec[0] - p1[0]) / p1v[0] if p1v[0] != 0 else (intersec[1] - p1[1]) / p1v[0]
    p2t = (intersec[0] - p2[0]) / p2v[0] if p2v[0] != 0 else (intersec[1] - p2[1]) / p2v[0]
    return (p1[2] - p2[2] + p1t * p1v[2] - p2t * p2v[2]) / (p1t - p2t) if p1t != p2t else None


if __name__ == '__main__':
    with (open('day24.txt') as log_file):
        points_velocities = [list(map(lambda c: tuple(map(D, c.split(', '))), line.strip().split(' @ ')))
                             for line in log_file]
    inspection_range, inside_intersections = [200000000000000, 400000000000000], 0
    # inspection_range, inside_intersections = [7, 27], 0
    for pc1, pc2 in combs(points_velocities, 2):
        p1, p1v, p2, p2v = pc1[0], pc1[1], pc2[0], pc2[1]
        p = intersection(line((p1[0], p1[1]), (p1v[0], p1v[1])), line((p2[0], p2[1]), (p2v[0], p2v[1])))
        if (p and inspection_range[0] <= p[0] <= inspection_range[1] and
                inspection_range[0] <= p[1] <= inspection_range[1] and not intersection_in_past(p1, p1v, p) and not
                intersection_in_past(p2, p2v, p)):
            inside_intersections += 1
            # print(f'Hailstone A: {p1} @ {p1v}')
            # print(f'Hailstone B: {p2} @ {p2v}')
            # print(f'Intersection: {p}')
    print(f'The number of intersections inside the inspection range is: {inside_intersections}')
    n = 0
    while n > -1:
        for x in range(n + 1):
            y = n - x
            for xv, yv in [(x, y), (-x, y), (x, -y), (-x, -y)]:
                p1, p1v = points_velocities[0][0], points_velocities[0][1]
                inter = None
                for p2, p2v in points_velocities[1:]:
                    p = intersection(line((p1[0], p1[1]), (p1v[0] - xv, p1v[1] - yv)),
                                     line((p2[0], p2[1]), (p2v[0] - xv, p2v[1] - yv)))
                    if not p:
                        break
                    if inter is None:
                        inter = p
                        continue
                    if inter != p:
                        break
                if p is None or p != inter:
                    continue
                zv = next_zv = None
                for p2, p2v in points_velocities[1:]:
                    next_zv = getZ(p1, (p1v[0] - xv, p1v[1] - yv, p1v[2]), p2,
                                   (p2v[0] - xv, p2v[1] - yv, p2v[2]), inter)
                    if zv is None:
                        zv = next_zv
                        continue
                    if next_zv != zv:
                        exit(1)
                        break
                if next_zv == zv:
                    z = p1[2] + ((inter[0] - p1[0]) / (p1v[0] - xv)) * (p1v[2] - zv) if p1v[0] - xv != 0\
                        else p1[2] + ((inter[1] - p1[1]) / (p1v[1] - vy)) * (p1v[2] - zv)
                    print(f'v=<{xv},{yv},{zv}>, p=<{inter[0]},{inter[1]},{z}>, s = {z + inter[0] + inter[1]}')
                    exit(0)
        n += 1
