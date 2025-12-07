
def bubbleSort(elements):
    size = len(elements)

    for i in range(size-1):
        #if the user passes an entire sorted list, then swapped = False becoz, inner loop will not execute as condition is not true and we will beak the outer loop.
        # this prevents checking over and over again through already swapped elements
        swapped = False #to prevent running loop again for already swapped elements(FLAG VARIABLE starts as Falseswapped = False #to prevent running loop again for already swapped elements(FLAG VARIABLE starts as False)
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True #if we find two elements out of order and swap them, we set the flag to True
                #or in python we can use element[j], element[j+1] = element[j+1], element[j]
        if not swapped: #At the end of the one full pass through outer loop, if swapped is still False, it means no swaps occurred.
            break #That means the list is already sorted → no need to continue looping.



if __name__ == "__main__":
    numbers_List = [10, 22, 7, 9, 85, 99]
    bubbleSort(numbers_List)
    print(numbers_List)
    