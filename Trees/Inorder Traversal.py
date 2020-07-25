class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        

    def inOrd(self, root):
        li = []
        def helper(root):
            if root:
                helper(root.left)
                li.append(root.val)
                helper(root.right)
        helper(root)
        return li