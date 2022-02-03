from fileinput import input
from functools import reduce


class Submarine:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


def move(sub, action):
    action = action.split()
    act = action[0]
    amm = int(action[1])
    if act == 'forward':
        return Submarine(sub.x + amm, sub.y)
    elif act == 'up':
        return Submarine(sub.x, sub.y + amm)
    elif act == 'down':
        return Submarine(sub.x, sub.y - amm)


print(reduce(
    move,
    map(
        lambda x: x.strip(),
        input()
    ),
    Submarine(0, 0)
))
