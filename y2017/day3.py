import math
from itertools import count


def spiral_steps(n):
    shell = int(math.floor(math.ceil(math.sqrt(n)) / 2))
    if shell == 0:
        return 0
    offset = (n - (2 * shell - 1) ** 2) % (2 * shell)
    return shell + abs(offset - shell)


def spiral_sum(n):
    # Let's just calculate the sequence until we get the answer
    a = {(0, 0): 1}
    i = j = 0
    for s in count(1, 2):  # odd numbers
        for (ds, di, dj) in [(0, 1, 0), (0, 0, -1), (1, -1, 0), (1, 0, 1)]:
            for _ in range(s + ds):
                i += di
                j += dj
                a[i, j] = sum(a.get((k, l), 0) for k in range(i - 1, i + 2) for l in range(j - 1, j + 2))
                if a[i, j] > n:
                    return a[i, j]


if __name__ == '__main__':
    with open('inputs/input3.txt') as f:
        num = int(f.read().strip())
        print spiral_steps(num)
        print spiral_sum(num)
