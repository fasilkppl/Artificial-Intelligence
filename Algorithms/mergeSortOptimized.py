def mergeSort(arr):
    if len(arr) <= 1:
        return
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    mergeSort(left)
    mergeSort(right)
    return merge_sort_list(left, right, arr)

def merge_sort_list(leftSorted, rightSorted, arr):

    i = j = k= 0
    len_a = len(leftSorted)
    len_b = len(rightSorted)
    
    while i < len_a and j < len_b:
        if leftSorted[i] <= rightSorted[j]:
            arr[k] = leftSorted[i]
            i += 1
            
        else :
            arr[k] = rightSorted[j]
            j += 1
        k += 1
    while i <len_a:
        arr[k] = leftSorted[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = rightSorted[j]
        j += 1
        k += 1
        
    return arr


if __name__ == "__main__":

    list1 = [5,10,23,44,12,21,18,89]


    mergeSort(list1)
    print (list1)
    