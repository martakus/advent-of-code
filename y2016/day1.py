#!/usr/bin/python
def day1(str):
    cmds = [s.strip() for s in str.split(',')]
    nums = [[(1j if c[0] is 'L' else -1j), int(c[1:])] for c in cmds]
    dir = 1j
    z = complex(0,0)
    visitedLocations = [0]
    firstDup = None
    for n in nums:
        dir *= n[0]  # turn
        for _ in range(n[1]):
            z += dir  # walk one unit
            if firstDup is None and z in visitedLocations:
                firstDup = z
            visitedLocations.append(z)
    part_b_solution = None
    if firstDup is not None:
        part_b_solution = int(abs(firstDup.real) + abs(firstDup.imag))
    return int(abs(z.real) + abs(z.imag)), part_b_solution


if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as f:
        print day1(f.read())
