class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def LCA(root, p, q):
 
    if root == None:
        return None
        
    if root.val == p.val or root.val == q.val:
        return root
    
    left = LCA(root.left,p,q)
    right = LCA(root.right,p,q)

    if left == None:
        return right
        
    if right == None:
        return left
        
    if left != None and right != None:
        return root


#      8
#    /   \
#   3    10
#  / \     \
# 1   6    14
#    /
#   5

tree = Node(8)               
tree.left = Node(3)
tree.right = Node(10)
tree.left.left = Node(1)
tree.left.right = Node(6)
tree.right.right = Node(14)

print(LCA(tree, 6,14 ))


# tree = Node(4)               
# tree.left = Node(2)
# tree.right = Node(7)
# tree.left.left = Node(1)
# tree.left.right = Node(3)
# tree.right.left = Node(6)
# tree.right.right = Node(9)



