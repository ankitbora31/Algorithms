"""
Recursion
it allows a function to call itself. fixed steps of code
get executed again and again for new values.
we also have to set criteria for deciding when the recursive
call ends
"""


# binary search using recursion

def bsearch(list, idx0, idxn, val):
    if idxn < idx0:
        return None
    else:
        midval = idx0 + ((idxn - idx0) // 2)

        if list[midval] > val:
            return bsearch(list, idx0, midval - 1, val)
        elif list[midval] < val:
            return bsearch(list, midval + 1, idxn, val)
        else:
            return midval


list1 = [8, 11, 2, 45, 382, 1, 9]
a = sorted(list1)
print(a)

print(bsearch(a, 0, 6, 382))
print(bsearch(a, 0, 6, 92))