class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lCA(root):
    
    if root == None:
            return None
        
    if p.val < root.val and q.val < root.val:
        return self.lowestCommonAncestor(root.left,p,q)
        
    elif p.val > root.val and q.val > root.val:
        return self.lowestCommonAncestor(root.right,p,q)
    
    else:
        return root
            

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

print(func(tree ))


# tree = Node(4)               
# tree.left = Node(2)
# tree.right = Node(7)
# tree.left.left = Node(1)
# tree.left.right = Node(3)
# tree.right.left = Node(6)
# tree.right.right = Node(9)



