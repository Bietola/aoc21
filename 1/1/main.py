from fileinput import input
from operator import sub
from functools import reduce

inp = list(map(int, input()))

print(sum(map(
    lambda x: reduce(sub, x),
    zip(inp[1:], inp))))
