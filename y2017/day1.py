#! /usr/bin/env python
""" Solution to Advent of Code 2017: Day 1 Puzzles
    Markus Foote

    Call me like this:
    $ ./day1.py input1.txt
    or
    $ python day1.py input1.txt
"""
import sys


def inverse_captcha(sequence):
    mask = [int(a) == int(b) for a, b in zip(sequence, ''.join([sequence[1:], sequence[0]]))]
    result = sum([int(s) if m else 0 for s, m in zip(sequence, mask)])
    return result


def inverse_captcha_half(sequence):
    halfway_index = len(sequence) / 2  # problem statement guarantees length is even
    mask = [int(a) == int(b) for a, b in zip(sequence, ''.join([sequence[halfway_index:], sequence[:halfway_index]]))]
    result = sum([int(s) if m else 0 for s, m in zip(sequence, mask)])
    return result


if __name__ == '__main__':
    with open(sys.argv[-1]) as f:  # I'm assuming there is only one input file and it is listed last
        for line in f:
            print inverse_captcha(line.strip())
            print inverse_captcha_half(line.strip())
