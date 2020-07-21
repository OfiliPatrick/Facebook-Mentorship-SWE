class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(self, head: ListNode) -> bool:     
        fast = head
        slow = head  
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next       
        mid = slow
        head_rh = self.reverseLL(mid)
        while head and head_rh:
            if head.val != head_rh.val:
                return False

            head = head.next
            head_rh = head_rh.next
        return True
        
def reverseLL(self,head):
    new_head = head
    last_seen = None
    while head:
        node_after = head.next
        head.next = last_seen
        last_seen = head
        head = node_after   
    return last_seen
        