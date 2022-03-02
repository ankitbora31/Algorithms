"""
SHELL SORT
it involves sorting elements which are away from each
other. we sort a large sub list of given list and go on
reducing the size of the list until all elements are
sorted.
"""


def shell_sort(input_list):
    gap = len(input_list)//2
    while gap>0:
        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i

            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j-gap
            input_list[j] = temp

        gap = gap//2

list1 = list(map(int, input().split()))
shell_sort(list1)
print(list1)