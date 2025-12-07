from util import time_it


@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index #A return statement immediately ends the function , Once a return is executed — the function stops running and goes back to where it was called.
    return -1

@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index: 
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find: #if number to find is big, look in the right side of array
            left_index = mid_index + 1 #we already checked middle element, so now we're checking after one element from middle element.
        else: #if number to find is small, look in the left side of array
            right_index = mid_index - 1 #we already checked middle element, so now we're checking before one element from middle element.

    return -1


def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

if __name__ == '__main__':

    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]


  # First search
    number_to_find = 45
    index1 = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    print(f"Number {number_to_find} found at index {index1}")

    # Second search
    number_to_find = 19
    index2 = binary_search(numbers_list, number_to_find)
    print(f"Number {number_to_find} found at index {index2}")