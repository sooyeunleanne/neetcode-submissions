"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        node_dict = {} # store old node --> new node

        old = head
        while old:
            new = Node(old.val)
            node_dict[old] = new
            old = old.next
        
        old = head
        while old:
            new = node_dict[old]
            new.next = node_dict[old.next] if old.next != None else None
            new.random = node_dict[old.random] if old.random != None else None
            old = old.next
        
        return node_dict[head]
