#/usr/bin/env python
from hashlib import md5
import sys
import random 

def day5a(code):
    doorcode = [];
    num = 0
    while len(doorcode) < 8:
        output = md5(code + str(num)).hexdigest()
        if output.startswith('00000'):
            doorcode.append(output[5])
        num += 1
        if num % 1000000 == 0:
            print num
    return doorcode

def day5b(code):
    doorcode = ['_' for i in range(8)];
    posfillorder = []
    num = 0
    while len(posfillorder) < 8:
        output = md5(code+str(num)).hexdigest()
        if output.startswith('00000'):
            pos = int(output[5],16)
            val = output[6]
            if pos in range(8) and pos not in posfillorder:
                doorcode[pos] = val
                posfillorder.append(pos)
             #   sys.stdout.write('Decrypting: {}\r'.format(''.join(doorcode)))
             #   sys.stdout.flush()
        num += 1
#        if num % 1000000 == 0:
#            print num
#            tempstr = doorcode
#            for i in range(8):
#               if tempstr[i] == '_':
#                    tempstr[i] = output[i+10]
#            sys.stdout.write('\rDecrypting: {}'.format(''.join(tempstr)))
#            sys.stdout.flush()
    print num
    return doorcode

if __name__ == '__main__':
    import sys
    print ''.join(day5b(sys.argv[1]))
