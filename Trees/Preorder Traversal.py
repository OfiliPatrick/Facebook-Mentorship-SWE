"""
Example

       8
     /   \
    3    10
   / \     \
  1   6    14

output = [8,3,1,6,10,14]

Steps
    
    Recursive Approach:
    1. For every node, process it.
    2. Visit its left subtree.
    3. Visit its right subtree.
    4. Time complexity is O(n) where n is the total number of nodes. Space complexity is O(h) where h is the height of the tree.

    Iterative Approach:
    1. For every node, add to a stack.
    2. Process the node and pop from the stack.
    3. Add its right and left child to the stack.
    4. Time complexity is O(n) ,Space complexity is also O(n) where n is the total number of nodes.

"""



class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def preOrdRec(root):
    output = []
    def helper(root):
        if root == None:
            return None

        output.append(root.val)
        helper(root.left)
        helper(root.right)
    
    helper(root)
    return output

def preOrdItr(root):
    output = []
    stack = [root]

    while stack:
        curr_node = stack.pop()
        output.append(curr_node.val)
        
        if curr_node.right:
            stack.append(curr_node.right)

        if curr_node.left:
            stack.append(curr_node.left)
    
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

# print(preOrdItr(tree))
# print(preOrdRec(tree))