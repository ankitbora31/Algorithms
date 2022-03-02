"""
INSERTION SORT
it involves finding the right place for a given element
in a sorted list. so in beginning we compare the first
two elements and sort them by comparing them. then we
pick the third element and find its proper position
among the previous two sorted elements. this way we
gradually go on adding more elements to the already sorted
list by putting them in their proper position.
"""


def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        j = i - 1
        nxt_element = input_list[i]

        while (input_list[j] > nxt_element) and j >= 0:
            input_list[j + 1] = input_list[j]
            j = j - 1
        input_list[j + 1] = nxt_element


list1 = [19, 2, 31, 45, 30, 11, 121, 27]
insertion_sort(list1)
print(list1)
