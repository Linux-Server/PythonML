class QuickFind:
    def __init__(self, num:int):
        self.arr = []
        for i in range(num):
            self.arr.append(i)

    def find(self, p, q):
        return self.arr[p] == self.arr[q]

    def union(self, p, q):
        pid = self.arr[p]
        qid = self.arr[q]
        for i,val in enumerate(self.arr):
            if val == pid:
                self.arr[i] = qid



quick = QuickFind(10)
quick.union(4,6)
print(quick.arr)
print(quick.find(4,6))