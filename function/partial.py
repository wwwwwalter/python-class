from functools import partial


def mod(n, m):
    return n % m


mod_by_100 = partial(mod, 100)

print(mod_by_100(7))
