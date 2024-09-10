'''
A merge sort code that uses recursive calls to mergesort function and a helper recombine function
'''
import rand


def merge_sort(arr):
    '''
        Function base case: Input array arr[] of length 1
        Other Case: Divides array arr[] into 2 parts,
        makes recursive calls to mergSort function,
        uses recombine function to merge the outputs of the 2 recursive calls
    '''
    if len(arr) == 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    '''
    Function that merges the 2 arrays: leftArr and rightArr in sorted order
    '''
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]
        right_index+=1

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]
        left_index+=1

    return merge_arr


if __name__ == "__main__":
    arr_in = rand.random_array([None] * 20)
    arr_out = merge_sort(arr_in)
    print(arr_out)
