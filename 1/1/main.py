from functools import reduce
from fileinput import input
from operator import sub

inp = list(map(int, input()))

print(sum(map(
    lambda x: reduce(sub, x),
    zip(inp[1:], inp)
)))
