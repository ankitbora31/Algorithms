"""
selection sort
in this we start by finding the minimum value in a given
list and move it to a sorted list. then we repeat the
process for each of the remaining elements in the unsorted
list. the next element entering the sorted list is compared
with the existing elements and placed at its correct position.
so at the end all the elements from the unsorted list
are sorted.
"""


def selection_sort(input_list):
    for idx in range(len(input_list)):

        min_idx = idx
        for j in range(idx + 1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j

        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]


l = [19, 2, 31, 45, 30, 11, 121, 27]
selection_sort(l)
print(l)

