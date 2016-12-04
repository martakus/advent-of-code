#!/usr/bin/python
def day1(str):
    cmds = [s.strip() for s in str.split(',')]
    i = complex(0,1)
    nums = [[(i if c[0] is 'L' else -i),int(c[1:])] for c in cmds]
    z = complex(0,0)
    for n in reversed(nums):
        z = n[0]*(n[1]*i + z)
    return (abs(z.real)+ abs(z.imag))

if __name__=='__main__':
    import sys
    print day1(' '.join(sys.argv[1:]))
