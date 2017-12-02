#!/usr/bin/python
def nextkey19(key,char):
    if key == 1:
        if char == 'D':
            return 4
        elif char == 'R':
            return 2
        else:
            return 1
    elif key == 2:
        if char == 'D':
            return 5
        elif char == 'L':
            return 1
        elif char == 'R':
            return 3
        else:
            return 2
    elif key == 3:
        if char == 'D':
            return 6
        elif char == 'L':
            return 2
        else:
            return 3
    elif key == 4:
        if char == 'U':
            return 1
        elif char == 'D':
            return 7
        elif char == 'R':
            return 5
        else:
            return 4
    elif key == 5:
        if char == 'U':
            return 2
        elif char == 'D':
            return 8
        elif char == 'L':
            return 4
        elif char == 'R':
            return 6
        else:
            return 5
    elif key == 6:
        if char == 'U':
            return 3
        elif char == 'D':
            return 9
        elif char == 'L':
            return 5
        else:
            return 6
    elif key == 7:
        if char == 'U':
            return 4
        elif char == 'R':
            return 8
        else :
            return 7
    elif key == 8:
        if char == 'U':
            return 5
        elif char == 'L':
            return 7
        elif char == 'R':
            return 9
        return 8
    elif key == 9:
        if char == 'U':
            return 6
        elif char == 'L':
            return 8
        return 9
    
def nextkeystar(key,char):
    if key == 1:
        if char == 'D':
            return 3
        return key
    elif key == 2:
        if char == 'D':
            return 6
        if char == 'R':
            return 3
        return key
    elif key == 3:
        if char == 'U':
            return 1
        elif char == 'D':
            return 7
        elif char == 'L':
            return 2
        else:
            return 4
    elif key == 4:
        if char == 'L':
            return 3
        elif char == 'D':
            return 8
        return 4
    elif key == 5:
        if char == 'R':
            return 6
        return 5
    elif key == 6:
        if char == 'U':
            return 2
        elif char == 'D':
            return 'A'
        elif char == 'L':
            return 5
        elif char == 'R':
            return 7
    elif key == 7:
        if char == 'U':
            return 3
        elif char == 'D':
            return 'B'
        elif char == 'L':
            return 6
        return 8
    elif key == 8:
        if char == 'U':
            return 4
        elif char == 'D':
            return 'C'
        elif char == 'L':
            return 7
        return 9
    elif key == 9:
        if char == 'L':
            return 8
        return 9
    elif key == 'A':
        if char == 'U':
            return 6
        elif char == 'R':
            return 'B'
        return 'A'
    elif key == 'B':
        if char == 'U':
            return 7
        elif char == 'D':
            return 'D'
        elif char == 'L':
            return 'A'
        return 'C'
    elif key == 'C':
        if char == 'U':
            return 8
        elif char == 'L':
            return 'B'
        return 'C'
    elif key == 'D':
        if char == 'U':
            return 'B'
        return 'D'

def day2(str):
    code = []
    for line in str.split('\n'):
        if line:
            key = 5
            for char in line:
                key = nextkeystar(key,char)
            code.append(key)
    return code

if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as f:
        print day2(f.read())
