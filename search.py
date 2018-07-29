"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    low_ptr = 0
    high_ptr = len(input_array) -1
    while (low_ptr <= high_ptr):
        print ("low_ptr = {0}, high_ptr = {1}".format(low_ptr,high_ptr))
        mid_ptr = (low_ptr + high_ptr) / 2
        if value < input_array[mid_ptr]:
            ''' use left slice '''
            high_ptr = mid_ptr - 1
        elif value > input_array[mid_ptr]:
            ''' use right slice '''
            low_ptr = mid_ptr + 1
        elif value == input_array[high_ptr]:
            ''' bingo '''
            return high_ptr
        
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)