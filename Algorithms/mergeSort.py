def mergeSort(arr):
    if len(arr) <= 1:
        return arr[1]
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    leftSorted = mergeSort(left)
    rightSorted = mergeSort(right)
    return merge_sort_list(leftSorted, rightSorted, sortedList)

def merge_sort_list(a, b, sortedList):

    i = j = 0
    len_a = len(a)
    len_b = len(b)
    
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sortedList.append(a[i])
            i += 1
        else :
            sortedList.append(b[j])
            j += 1
    while i <len_a:
        sortedList.append(a[i])
        i += 1
    while j < len_b:
        sortedList.append(b[j])
        j += 1
    return sortedList


if __name__ == "__main__":
    sortedList = []
    list1 = [5,18,62,99]
    list2 = [4, 41,55,66]

    merge_sort_list(list1, list2, sortedList)
    print (sortedList)
    