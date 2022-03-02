"""
backtracking is a form of recursion. but it involves
choosing only option out of any possibilities. we begin
by choosing an option and backtrack from it, if we reach
a state where we conclude that this specific option does
not give the required solution. we repeat these steps by
going across each available option until we get the desired
solution
"""

# example

def permute(list, s):
    if list == 1:
        return s
    else:
        return [y + x for y in permute(1,s) for x in permute(list-1, s)]

print(permute(1, ['a', 'b', 'c']))
print(permute(2, ['a', 'b', 'c']))