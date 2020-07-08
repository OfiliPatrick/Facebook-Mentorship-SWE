"""
Examples 
    For Singly Linked List:
    - [1,2,1]   =>  True
    - [1,2,3], 1  =>  False
    - [1,1] , 1  =>  True
    - [1] => True
  
Steps
    For Singly Linked List:
     1. Extract all values into array
     2. Have 2 pointers converge from the first and last index while checking for matching values
     3. Return False if mismatch else return true on successful convergence
     4. Time complexity is O(n), Space complexity is O(n)

    For Doubly Linked List (follow up):
     1. Get the total length of the linked list
     2. Have 2 pointers converge length/2 times from the head and tail node while checking for matching values
     3. Return False if mismatch else return true on successful convergence
     4. Time complexity is O(n), Space complexity is O(n)

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
# DoublyLL.next.next = DNode(5)
# DoublyLL.next.next.prev = DoublyLL.next

# print(isPalindromeSingly(SinglyLL))
# print(isPalindromeDoubly(DoublyLL))



        

