class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def preOrd(self, root):
        li = []
        def helper(root):
            if root:
                print(root.val)
                li.append(root.val)
                helper(root.left)
                helper(root.right)
        helper(root)
        return li