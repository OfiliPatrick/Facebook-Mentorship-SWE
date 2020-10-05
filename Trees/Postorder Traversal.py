"""
Example

       8
     /   \
    3    10
   / \     \
  1   6    14

output = [1,6,3,14,10,8]

Steps

    Recursive Approach:
    1. For every node, Visit its left subtree.
    2. Visit its right subtree.
    3. Process the node.
    4. Time complexity is O(n) where n = total number of nodes. Space complexity is O(h) where h is the height of the tree.

    Iterative Approach:
    1. For every node, add to a stack.
    2. Process the node and pop from the stack.
    3. Add its left and right child to the stack.
    4. Reverse the final output.
    4. Time complexity is O(n) ,Space complexity is also O(n) where n is the total number of nodes.

"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def postOrdRec(root):
    output = []
    def helper(root):
        if root == None:
            return None

        helper(root.left)
        helper(root.right)
        output.append(root.val)

    helper(root)
    return output

# post order is the reverse of preorder taking right to left leaves

def postOrdItr(root):
    output = []
    
    stack = [root]

    while stack:
        curr_node = stack.pop()
        output.append(curr_node.val)
       
        if curr_node.left:
            stack.append(curr_node.left)

        if curr_node.right:
            stack.append(curr_node.right) 

    output.reverse()
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

# print(postOrdItr(tree))
# print(postOrdRec(tree))