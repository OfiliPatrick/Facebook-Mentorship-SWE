"""
Example

       8
     /   \
    3    10
   / \     \
  1   6    14

output = [1,3,6,8,10,14]

Steps

    Recursive Approach:
    1. For every node, visit its left subtree.
    2. Process the node.
    3. Visit its right subtree.
    4. Time complexity is O(n) where n is the total number of nodes. Space complexity is O(h) where h is the height of the tree.

    Iterative Approach:
    1. Start from the root and keep appending left nodes to a stack until no more.
    2. Then pop from stack and process the node popped.
    3. Add right child of processed node to stack.
    4. Time complexity is O(n) ,Space complexity is also O(n) where n is the total number of nodes.

"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def inOrdRec(root):
    output = []
    def helper(root):
        if root:

            helper(root.left)
            output.append(root.val)
            helper(root.right)

    helper(root)
    return output

def inOrdItr(root):
    stack = []
    output = []

    while stack or root:
        if root:
            stack.append(root)
            root = root.left

        else:
            root = stack.pop()
            output.append(root.val)
            root = root.right 
   
    return output

#      8
#    /   \
#   3    10
#  / \     \
# 1   6    14

# tree = Node(8)               
# tree.left = Node(3)
# tree.right = Node(10)
# tree.left.left = Node(1)
# tree.left.right = Node(6)
# tree.right.right = Node(14)

# print(inOrdItr(tree))
# print(inOrdRec(tree))