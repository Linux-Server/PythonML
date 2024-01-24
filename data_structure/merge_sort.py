arr = [1,3,5,7,2,4,6]
aux = [1,3,5,7,2,4,6]

low = 0
hi = 6
mid = 3


        
print(arr)
        
    
class MergeSort:
    
    def merge(self, arr,aux,low,mid,hi):
        
        #low = 0
        #hi = 6
        #mid = 3
        i = low
        j = mid+1


        for (k, val) in enumerate(arr):
            # Edge cases : if i>mid => j++
            print(k)
            if i>mid:
                arr[k] = aux[j]
                j+= 1
            elif j>hi:
                arr[k] = aux[i]
                i+= 1
            elif aux[i] < aux[j]:
                arr[k] = aux[i]
                i+= 1
            else:
                aux[j] < aux[i]
                arr[k] = aux[j]
                j+= 1
        