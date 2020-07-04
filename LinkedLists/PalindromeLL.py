"""
Steps
Can i assume that the node will always be in the list

1. 
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
      
# Palindrome check for Singly Linked List
def isPalindromeSingly(head):
    all_vals = []
    while head:
        all_vals.append(head.val)
        head = head.next
    first = 0
    last = len(all_vals) - 1  
    while first < last:
        if all_vals[first] == all_vals[last]:
            first += 1
            last -= 1    
        else:
            return False

    return True

    

# Palindrome check for Singly Linked List  
def isPalindromeDoubly(head):
    new_head = head
    length = 0
    tail = None
    while head:
        if head.next == None:
            tail = head
        length += 1
        head = head.next

    while length > length // 2:
        if new_head.val == tail.val:
            new_head = new_head.next
            tail = tail.prev
            length -= 2
        else:
            return False
    return True


#Test Case1 :  1 -> 2 -> 3 -> 4
SinglyLL = SNode(1)
SinglyLL.next = SNode(2)
SinglyLL.next.next = SNode(3)
SinglyLL.next.next.next = SNode(4)

print(isPalindromeSingly(SinglyLL))



# Test Case 2
#     ->     ->
#  5      6      7
#     <-     <-
DoublyLL = DNode(5)
DoublyLL.next = DNode(6)
DoublyLL.next.prev = DoublyLL
DoublyLL.next.next = DNode(7)
DoublyLL.next.next.prev = DoublyLL.next

print(isPalindromeDoubly(DoublyLL))



        

