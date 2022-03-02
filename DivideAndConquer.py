"""
Divide and Conquer
in this problem is divided into smaller sub problems
and then each problem is solved independently. when we
keep on dividing the sub problems into even smaller
sub problems we may eventually reach a stage where no more
division is possible. the solutions of all sub problems
is merged into one to obtain the solution of original
problem
"""
# binary search implementation uses divide and conquer approach


def bsearch(list, val):
    list_size = len(list) - 1

    idx0 = 0
    idxn = list_size
    # Find the middle most value

    while idx0 <= idxn:
        midval = (idx0 + idxn) // 2

        if list[midval] == val:
            return 'at index {}'.format(midval)
        # Compare the value the middle most value
        if val > list[midval]:
            idx0 = midval + 1
        else:
            idxn = midval - 1

    if idx0 > idxn:
        return None


# Initialize the sorted list
list1 = [2, 7, 19, 34, 53, 72]

# Print the search result
print(bsearch(list1, 72))
print(bsearch(list1, 11))

print('-----------------------')

# sequential search

a = [2, 3, 1, 5, 83, 42, 29, 9]

def to_find(x):
    for i in range(len(a)):
        if a[i] == x:
            print('fount at index {}'.format(i))
        else:
            print('not present at index {}'.format(i))

to_find(29)