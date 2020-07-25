class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def numNodes(root):
    num_nodes = 1
    def inOrdTrav(root,num_nodes):
        if root:
            inOrdTrav(root.left, num_nodes + 1)
            inOrdTrav(root.right, num_nodes+1)

    inOrdTrav(root,num_nodes)

    return num_nodes


#      8 
#    /   \
#   3    10
#  / \     \
# 1   6    14

tree = Node(8)               
tree.left = Node(3)
tree.right = Node(10)
tree.left.left = Node(1)
tree.left.right = Node(6)
tree.right.right = Node(14)

print(numNodes(tree))