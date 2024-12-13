import re
from math import gcd

def arcading(data: str, part2: bool=False) -> int:
    arcade_re = r'A:\sX\+(?P<a>\d+),\sY\+(?P<d>\d+)\s.*B:\sX\+(?P<b>\d+),\sY\+(?P<e>\d+)\s.*X=(?P<c>\d+),\sY=(?P<f>\d+)'
    tokens = 0
    for arcade in data.split('\n\n'):
        (a, d, b, e, c, f), t, sols = map(int, re.search(arcade_re, arcade).groups()), 0, []
        c, f = (c + 10000000000000, f + 10000000000000) if part2 else (c, f)
        if c % gcd(a,b) != 0 or f % gcd(d,e) != 0:
            continue
        x = (c*e - f*b) / (a*e - b*d) if a*e - b*d != 0 else 0
        y = (c*d - f*a) / (b*d - a*e) if b*d - a*e != 0 else 0
        if x.is_integer() and y.is_integer():
            tokens += 3 * int(x) + int(y)
    return tokens


def solve(data: str, part: int):
    if part == 1:
        return arcading(data)
    if part == 2:
        return arcading(data, True)
    return [arcading(data), arcading(data, True)]
