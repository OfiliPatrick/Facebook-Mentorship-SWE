"""
Question - Delete a given node in a linked list without the head pointer

Examples 
    - [1,2,3,4] , 3  =>  [1,2,4]
    - [1,2], 1  =>  [2]
    - [5,6,7] , 7  =>  [5,6]
    (Given node cannot be tail node for singly Linked List)
  
Steps
    For Singly Linked List:
     1. Replace the value of the given node with the value of the node after
     2. Let the given node point to the node after its next node
     3. Time complexity is O(1), Space complexity is O(1)

    For Doubly Linked List (follow up):
     1. Get the nodes before and after the given node
     2. Let the node before point to the node after and vice versa
     3. Time complexity is O(1), Space complexity is O(1)
    
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
        

def SinglyDelete(node):
    node.val = node.next.val
    node.next = node.next.next

def DoublyDelete(node):
    if node.next == None:
        prev_node = node.prev
        prev_node.next = None
    else:
        prev_node = node.prev
        next_node = node.next_node
        prev_node.next = next_node
        next_node.prev = prev_node


#Test Case1 :  1 -> 2 -> 3 -> 4 -> None

# SinglyLL = SNode(1)
# SinglyLL.next = SNode(2)
# SinglyLL.next.next = SNode(3)
# SinglyLL.next.next.next = SNode(4)

# Test Case 2

#     ->     ->     ->
#  5      6      7      None
#     <-     <-     <-

# DoublyLL = DNode(5)
# DoublyLL.next = DNode(6)
# DoublyLL.next.prev = DoublyLL
# DoublyLL.next.next = DNode(7)
# DoublyLL.next.next.prev = DoublyLL.next


# SinglyDelete(SinglyLL)
# print(printAll(SinglyLL))
# DoublyDelete(DoublyLL.next.next)
# print(printAll(DoublyLL))



        

