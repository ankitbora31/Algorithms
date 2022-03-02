"""
QUICK SORT
it is a divide and conquer algorithm.
it picks an element as pivot and partition the given
array around the the picked pivot. there are many approaches
of quick sort that pick pivot in different ways.
"""


def partition(arr, low, high):
    i = low-1
    pivot = arr[high]

    for j in range(low,high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1


def quickSort(arr,low,high):
    if len(arr)==1:
        return arr
    if low<high:
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)


arr = list(map(int, input().split()))
n = len(arr)
quickSort(arr,0,n-1)
print('sorted array is:')
b = []
for i in range(n):
    b.append(arr[i])
print(b)
