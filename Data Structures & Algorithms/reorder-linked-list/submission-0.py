# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        i = 0
        cur = head
        
        nodes = {}
        
        while cur:
            nodes[i] = cur

            i += 1
            cur = cur.next
        
        n = len(nodes)
        for i in range(n // 2):
            left = nodes[i]
            right = nodes[n - 1 - i]

            left.next = right
            right.next = nodes[i + 1] if (i + 1) != (n - 1 - i) else None
        
        if n % 2 == 1: # if there are odd nodes
            nodes[n // 2].next = None