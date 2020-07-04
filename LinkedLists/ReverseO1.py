class SNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def printAll(head):
    all_vals = []
    while head:
        all_vals.append(head.val)
        head = head.next
    return all_vals

def reverseLL(head):
    new_head = head
    last_seen = None
    while head:
        node_after = head.next
        head.next = last_seen
        last_seen = head
        head = node_after   
    return last_seen
    

#Test Case1 :  1 -> 2 -> 3 -> 4
SinglyLL = SNode(1)
SinglyLL.next = SNode(2)
SinglyLL.next.next = SNode(3)
SinglyLL.next.next.next = SNode(4)

out = reverseLL(SinglyLL)
print(printAll(out))
