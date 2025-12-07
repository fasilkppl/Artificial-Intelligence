

def insertionSort(elements):
    for i in range(1, len(elements)):# first element is already sorted, so we start from first index
        anchor = elements[i] #setting second element as anchor
        j = i - 1 #setting j one index less than i, eg: j = 3, i = 2
        
        while j >= 0 and elements[j] > anchor: # if first element is greater than second element
            elements[j+1] = elements[j] # copy first element to second element
            j = j - 1 # it keeps moving j left (j = j - 1) until it finds the right position for the anchor, or it reaches the start of the list.
        
        elements[j+1] = anchor # after coming outta the loop, copy second element to first element.


if __name__ == '__main__':
    elements = [34, 2, 45, 23, 10]
    insertionSort(elements)
    print(elements)
    
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    for item in tests:
        insertionSort(item)
        print(item)
        


'''[2, 34, 45, 23, 10]
3rd iteration:
i = 3 → anchor = 23

Left side = [2, 34, 45]

Compare 23 with 45 → move 45 right

Compare 23 with 34 → move 34 right

Compare 23 with 2 → 2 < 23 → stop

Insert 23 after 2'''