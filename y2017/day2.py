#! /usr/bin/env python
""" Solution to Advent of Code 2017: Day 2 Puzzles
    Markus Foote, 2017
"""
import sys


def check_sum(st):
    accumulator = 0
    for l in st.strip().split('\n'):
        numbers = [int(a) for a in l.strip().split('\t')]
        accumulator += max(numbers) - min(numbers)
    return accumulator


def check_divide(st):
    accumulator = 0
    for l in st.strip().split('\n'):
        numbers = [int(a) for a in l.strip().split('\t')]
        divisible = [any([float(a) / float(b) == int(float(a) / float(b))
                          if a != b else False for a in numbers]) for b in numbers]
        accumulator += sum([sum([a/n if (float(a) / float(n) == int(float(a) / float(n)) and a != n)
                                 else 0 for a in numbers]) if r else 0 for n, r in zip(numbers, divisible)])
    return accumulator


if __name__ == '__main__':
    if len(sys.argv) == 1:  # No file provided as input
        with open('./inputs/input2.txt') as f:
            s = f.read()
            print check_sum(s)
            print check_divide(s)
    else:
        with open(sys.argv[-1]) as f:
            with f.read() as line:
                print check_sum(line.strip())
                print check_divide(line.strip())
