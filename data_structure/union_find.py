class UnionFind():
    def __init__(self, num):
        self.arr = []
        for i in range(num):
            self.arr.append(i)


    def check_find(self, p,q):
        return self.arr[p] == self.arr[q]


    def perform_union(self, p, q):
        pid = self.arr[p]
        qid = self.arr[q]
        for (i,val) in enumerate(self.arr):
            if val == pid:
                self.arr[i] = qid




unions = UnionFind(10)
print(unions.arr)
print(unions.check_find(1,4))

unions.perform_union(1,4)
print(unions.arr)
