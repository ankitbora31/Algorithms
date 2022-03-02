"""
sorting means arranging the data in particular format
sorting algorithm specifies the way to arrange data in a
particular order.

Bubble sort== it is a comparison based algorithm in which
each pair of adjacent elements is compared and the elements
are swapped if they are not in order.
"""


def bubble_sort(list):
    for i in range(len(list) - 1, 0, -1):
        for idx in range(i):
            if list[idx] > list[idx + 1]:
                temp = list[idx]
                list[idx] = list[idx + 1]
                list[idx + 1] = temp


list = [19, 2, 31, 45, 8, 11, 231, 28]
bubble_sort(list)
print(list)
