import cPickle
import md5
import random

def hash(key):
    hash = md5.md5()
    hash.update(cPickle.dumps(key))
    return int(hash.hexdigest(), 16)

class HashMap:
    def __init__(self):
        self.n = 0
        self.table = (1 << self.n) * [None]

    def mask(self):
        return (1 << self.n) - 1

    def insert(self, key, value):
        origP = self.size()
        origSize = 1 << self.n
        kh = hash(key)
        index = oldIndex = kh & self.mask()
        if self.table[index] is None:
            self.table[index] = (kh, value)
            return
        # Bump up self.n until no more collision
        oldkh, _ = self.table[index]
        if oldkh == kh:
            self.table[index] = (kh, value)
            return
        while (oldkh ^ kh) & self.mask() == 0:
            self.n += 1
        # Grow the table with empty new locations
        self.table += ((1 << self.n) - origSize) * [None]

        # move everybody to their new locations
        for i in range(origSize):
            if self.table[i] is not None:
                tmpkh, tmpvalue = self.table[i]
                index = tmpkh & self.mask()
                self.table[i] = None
                self.table[index] = (tmpkh, tmpvalue)

        # put the new guy in place
        index = kh & self.mask()
        assert self.table[index] is None
        self.table[index] = (kh, value)

    def size(self):
        p = 0
        for i in range(1 << self.n):
            if self.table[i] is not None:
                p += 1
        return p

    def get(self, key):
        kh = hash(key)
        index = kh & self.mask()
        x = self.table[index]
        if x is None:
            return None
        return x[1]

map = HashMap()
map.insert(1, 2)
map.insert(3, 4)
assert map.get(1) is 2, map.get(1)
assert map.get(3) is 4, map.get(3)

N = 100
d = {1: 2, 3: 4}
for i in range(N):
    k = random.random()
    v = random.random()
    d[k] = v
    map.insert(k, v)

for k in d.keys():
    assert d[k] == map.get(k), (k, d[k], map.get(k))

assert map.size() == N + 2
print map.n
