#!/usr/bin/python
import string 
import re
def wrap(c):
    if c < ord('a'):
        return chr(c+26)
    if c > ord('z'):
        return chr(c-26)
    return chr(c)

def cipher(message,shift):
    spaces = re.finditer('-',message)
    message = [ord(c)+shift for c in message]
    message = [wrap(c) for c in message]
    for s in spaces:
        message[s.start()]=' '
    message = ''.join(message)
    return message

def day4a(str):
    counter = 0
    for line in str.split('\n'):
        if line: #Only continues if line is non-empty (ignores last LF/CR in file)
            sectorID = int(line[line.rfind('-')+1:line.find('[')])
            roomID = line[:line.rfind('-')]
            checksum = line[line.find('[')+1:-1]
            roomLetters = ''.join(roomID.split('-'))
            counts = [roomLetters.count(s) for s in string.lowercase]
            calcsum = []
            while len(calcsum) < 5:
                calcsum.append(string.lowercase[counts.index(max(counts))])
                counts[counts.index(max(counts))]=0
            if checksum.startswith(''.join(calcsum)):
                counter += sectorID
                #and also decrypt name
                shift = sectorID % 26 # shifting 26 times is no shift at all!
                roomName = cipher(roomID,shift)
                if roomName.startswith('north'):
                    print roomName, sectorID # I'll have to manually read these to find North Pole Objects
    return counter

if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as f:
        print day4a(f.read())
    
