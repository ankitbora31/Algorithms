"""
BUBBLE SORT
it works by repeatedly stepping through the list to be
sorted, comparing each pair of adjacent items and swapping
item if they are in wrong order.
"""


def bubble(input_arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if swapped == False:
            break

arr = list(map(int, input().split()))
bubble(arr)
for i in range(len(arr)):
    print("{}".format(arr[i]), end=" ")