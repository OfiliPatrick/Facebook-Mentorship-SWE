class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

    def levelOrd(self, root):
        import collections
        queue = collections.deque([root])
        seen = collections.defaultdict(bool)
        out = []
        while queue:
            curr_node = queue.popleft()
            seen[curr_node] = seen
            out.append(curr_node.val)
            children = [curr_node.left, curr_node.right]
            for child in children:
                if child:
                    queue.append(child)
                    seen[child] = True
        return out