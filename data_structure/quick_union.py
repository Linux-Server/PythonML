class QuickUnion:
    def __init__(self, num):
        self.arr = []
        for i in range(num):
            self.arr.append(i)

    def root(self, i):
        while (i != self.arr[i]):
            i = self.arr[i]
        return i


    def connected(self, p , q):
        return self.root(p) == self.root(q)


    def union(self, p, q):
        pr = self.root(p)
        qr = self.root(q)
        id[pr] = qr



quick_union = QuickUnion(10)
print(quick_union.arr)
