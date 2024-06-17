from math import atan, degrees, hypot
from sys import stdin

for line in stdin:
    a, b, s, m, n = map(int, line.split())
    if a == 0:
        break

    v_x = m * a / s
    v_y = n * b / s

    v = round(hypot(v_x, v_y), ndigits=2)
    A = round(degrees(atan(v_y / v_x)), ndigits=2)

    print('%.2f %.2f' % (A, v))
