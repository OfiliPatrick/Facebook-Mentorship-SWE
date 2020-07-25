class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def bstSearch(self, root, key):
        if root == None:
            return False

        elif root.val == key:
            return True

        else:
            if key < root.val:
                return self.binTreeSearch(root.left, key)
                
            else:
                return self.binTreeSearch(root.right, key)
