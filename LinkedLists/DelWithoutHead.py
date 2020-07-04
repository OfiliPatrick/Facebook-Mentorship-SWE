"""
Steps
Can i assume that the node will always be in the list

1. 

2.

3.

4.

"""


class SNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class DNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

#helper function to print all elements in the list
def printAll(head):
    all_vals = []
    while head:
        all_vals.append(head.val)
        head = head.next

    return all_vals
        
# Deletion for Singly Linked List, given node cannot be tail node
def SinglyDelete(node):
    node.val = node.next.val
    node.next = node.next.next

#Test Case1 :  1 -> 2 -> 3 -> 4
SinglyLL = SNode(1)
SinglyLL.next = SNode(2)
SinglyLL.next.next = SNode(3)
SinglyLL.next.next.next = SNode(4)

# SinglyDelete(SinglyLL.next.next.next)
# print(printAll(SinglyLL))


# Deletion for DoublyLinked List
def DoublyDelete(node):
    if node.next == None:
        prev_node = node.prev
        prev_node.next = None
    else:
        prev_node = node.prev
        next_node = node.next_node
        prev_node.next = next_node
        next_node.prev = prev_node


# Test Case 2

#     ->     ->
#  5      6      7
#     <-     <-
DoublyLL = DNode(5)
DoublyLL.next = DNode(6)
DoublyLL.next.prev = DoublyLL
DoublyLL.next.next = DNode(7)
DoublyLL.next.next.prev = DoublyLL.next

# DoublyDelete(DoublyLL.next.next)
# print(printAll(DoublyLL))



        

