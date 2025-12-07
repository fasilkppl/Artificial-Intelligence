def swap(a, b, arr): #swaps any two inputed index
    temp = 0
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp



def partition(elements, start, end):
    pivot_index = start #pivot is always the first element.
    pivot = elements[pivot_index]
    
    while start < end :
        while start < len(elements)-1 and elements[start] <= pivot: # checking smaller elements than pivot for moving pivot forward.(if larger element found we need to stop.)
            start += 1
        while elements[end] > pivot: # checking larger elements than pivot for moving pivot backward.(if smaller element than pivot found we need to stop.)
            end -= 1
        
        if start < end : 
            swap(start, end, elements) # after start pointer moving forward and end pointer moving backward, once they cross swap.
    #if start > end it means start and end pointer crossed.
    swap(pivot_index, end, elements) #after swapping, again swap end pointer element with pivot element
    
    return end

def quickSort(elements, start, end):#recursively sorting partitions left and right side
    if start < end:
        partition_index = partition(elements, start, end)
        quickSort(elements, start, partition_index - 1)
        quickSort(elements, partition_index + 1, end)

    
if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    quickSort(elements, 0, len(elements)-1)
    print(elements)
    
    #testing all test cases.
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    for item in tests:
        quickSort(item, 0, len(item)-1)
        print(item)
