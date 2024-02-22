class MergeSort():
    def __init__(self, arr):
        self.arr = arr
        self.aux = arr

    def merge(self,lo=0,mid=3,hi=7):
        i = lo
        j = mid+1
        for index,value in enumerate(self.aux):
            if self.aux[i] < self.aux[j]:
                self.arr[index] = self.aux[index]
            else:
                self.arr[index] = self.aux[index]








my_arr = [2,4,6,8, 1,3,5,7]
merge = MergeSort(my_arr)
print(merge.arr)
merge.merge()
print(merge.arr)
