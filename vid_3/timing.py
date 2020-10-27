import numpy as np
import timeit

def bubble_sort(arr):
    '''
    Sorts the list or array arr using bubble sort.

    Input: arr (list or array): the array to sort
    Output: sorted_arr (list): a copy of arr, with elements sorted in order
    '''
    # Make a copy first
    sorted_arr = arr.copy()
    counter = 1
    N = len(sorted_arr)

    # Keep looping over the list until there are no more swaps
    while True:
        # Keep track of whether we've swapped anything this time
        swapped = False

        # Compare each consecutive pair of elements
        for i in range(N-counter):
            if sorted_arr[i] > sorted_arr[i+1]:
                # Swap!
                sorted_arr[i], sorted_arr[i+1] = sorted_arr[i+1], sorted_arr[i]
                swapped = True

        # The next largest element is now at the correct place, we don't need to check it anymore
        counter += 1

        # If at this point swapped is still False, we can finish
        if not swapped:
            return sorted_arr
        
# Merge sort
def merge(arr1, arr2):
    '''
    Merge 2 sorted lists into one sorted list.
    '''
    sorted_list = []

    # Loop until the full list is formed, start at index 0 for both lists
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        # Compare the items at the current locations for both lists
        if arr1[i] < arr2[j]:
            sorted_list.append(arr1[i])
            i += 1
        else:
            sorted_list.append(arr2[j])
            j += 1

    # Add any remaining elements in arr1 or arr2 to the end
    sorted_list.extend(arr1[i:])
    sorted_list.extend(arr2[j:])
    return sorted_list


def merge_sort(arr):
    '''
    Recursive merge sort on an array or list of numbers.
    '''
    # Bottom of the recursion
    if len(arr) == 1:
        return arr

    # Recursively merge sort both halves
    arr1 = merge_sort(arr[:len(arr) // 2])
    arr2 = merge_sort(arr[len(arr) // 2:])

    # Merge the 2 sorted halves
    sorted_arr = merge(arr1, arr2)
    return sorted_arr


rng = np.random.default_rng()
n = 2000
arr = rng.integers(1, n+1, size=n)

my_code = '''
arr = rng.integers(1, n+1, size=n)

bubble_sort(arr)
'''

t = timeit.timeit(my_code, number=10, globals=globals())
print(t/10)
