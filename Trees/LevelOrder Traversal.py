"""
Example

       8
     /   \
    3    10
   / \     \
  1   6    14

output = [[8], [3, 10], [1, 6, 14]]

Steps
    1. For every node, add to a queue.
    2. Process the node and pop from the front of the queue.
    3. Add its left and right child to the queue.
    4. Time complexity is O(n), Space complexity is also O(n) where n is the total number of nodes.

"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

def levelOrder(root):
    import collections
    output = []
    queue = collections.deque([root])
    
    while queue:
        curr_level = []
        num_of_nodes = len(queue)
        
        for i in range(num_of_nodes):
            curr_node = queue.popleft()
            curr_level.append(curr_node.val)   
            
            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)

        output.append(curr_level)  
    
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

# print(levelOrder(tree))