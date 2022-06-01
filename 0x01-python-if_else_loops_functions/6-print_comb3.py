#!/usr/bin/python3
for m in range(0, 100):
    a, b = m // 10, m % 10
    if m // 10 < m % 10:
        if m < 89:
            print("{:02d}".format(m), end=', ')
        else:
            print("{:d}".format(m))
