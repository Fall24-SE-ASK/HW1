'''
A merge sort code that uses recursive calls to mergesort function and a helper recombine function
'''
import rand


def mergeSort(arr):
    '''
        Function base case: Input array arr[] of length 1
        Other Case: Divides array arr[] into 2 parts, and makes recursive calls to mergSort function, 
        and uses recombine function to merge the outputs of the 2 recursive calls
    '''
    if len(arr) == 1:
        return arr

    half = len(arr) // 2

    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))


def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            rightIndex += 1
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
        else:
            leftIndex += 1
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]

    for i in range(rightIndex, len(rightArr)):
        mergeArr[leftIndex + rightIndex] = rightArr[i]

    for i in range(leftIndex, len(leftArr)):
        mergeArr[leftIndex + rightIndex] = leftArr[i]

    return mergeArr


arr = rand.random_array([None] * 20)
arr_out = mergeSort(arr)

print(arr_out)
