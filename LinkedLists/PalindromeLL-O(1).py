"""
Examples 
    For Singly Linked List:
    - [1,2,1]   =>  True
    - [1,2,3], 1  =>  False
    - [1,1] , 1  =>  True
    - [1] => True
  
Steps
    1. Get the middle of the linked list.
    2. Reverse right half of the list.
    3. Compare left half of the list with its reversed right half.
    4. Time complexity is O(n), Space complexity is O(1). 
"""

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def isPalindrome(head):    
    fast = head
    slow = head  
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next       
    mid = slow
    head_rh = reverseLL(mid)
    while head and head_rh:
        if head.val != head_rh.val:
            return False
        head = head.next
        head_rh = head_rh.next
    return True
        
def reverseLL(head):
    new_head = head
    last_seen = None
    while head:
        node_after = head.next
        head.next = last_seen
        last_seen = head
        head = node_after   
    return last_seen


        
# testLL = ListNode(1)
# testLL.next = ListNode(2)
# testLL.next.next = ListNode(2)
# testLL.next.next.next = ListNode(1)
# print(isPalindrome(testLL))
