import sys

import demo

print(demo.__doc__)
pl = sys.path
for index, path in enumerate(pl):
    print(index, path)