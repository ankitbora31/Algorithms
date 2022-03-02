"""
BFS
it traverses a graph breadth ward motion and uses a
queue to remember to get the next vertex to start a search,
when a dead end occurs in any iteration.
"""

import collections


class Graph:
    def __init__(self, dict1=None):
        if dict1 is None:
            dict1 = {}
        self.dict1 = dict1


def bfs(Graph, startNode):
    seen, queue = set([startNode]), collections.deque([startNode])
    while queue:
        vertex = queue.popleft()
        marked(vertex)
        for node in Graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)


def marked(n):
    print(n)


dict1 = {"a": set(["b", "c"]),
                "b": set(["a", "d"]),
                "c": set(["a", "d"]),
                "d": set(["e"]),
                "e": set(["a"])
         }


bfs(dict1, 'a')