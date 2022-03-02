"""
Tree Traversal Algorithms
Traversal is a process to visit all nodes of a tree and
may print their values too. because, all nodes are
connected via edges(links) we always start from the root
(head) node. that is, we cannot randomly access a node
in a tree. there are three ways which we use to traverse
a tree===
1. in-order traversal -- left,root,right
2. pre-order traversal -- root, left, right
3. post-order traversal -- left, right, root
"""

# in order traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()

    def inOrderTraversal(self, root):
        res = []
        if root:
            res = self.inOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.inOrderTraversal(root.right)
        return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inOrderTraversal(root))
