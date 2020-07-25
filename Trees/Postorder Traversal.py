class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def postOrd(self, root):
        li = []
        def helper(root):
            if root:
                helper(root.left)
                helper(root.right)
                li.append(root.val)
        helper(root)
        return li