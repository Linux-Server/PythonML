class QuickFind:

    def __init__(self, num):
        self.arr = []
        for i in range(0,num):
            self.arr.append(i)

    def is_connected(self, index_p,index_q):
        return self.arr[index_p] == self.arr[index_q]


    def union(self, index_p, index_q):
        value_p = self.arr[index_p]
        value_q = self.arr[index_q]
        for i in range(len(self.arr)):
            if value_p == self.arr[i]:
                self.arr[i] = value_q



quick = QuickFind(10)
print(quick.arr)
print(quick.is_connected(1,2))
quick.union(4,3)
quick.union(3,8)

print(quick.arr)
