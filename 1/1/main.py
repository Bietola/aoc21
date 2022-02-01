import fileinput
from functools import reduce
from operator import sub

inp = list(map(
    int,
    fileinput.input()
))

print(sum(
    map(
        lambda t: reduce(sub, t),
        zip(inp[1:], inp)
    )
))
