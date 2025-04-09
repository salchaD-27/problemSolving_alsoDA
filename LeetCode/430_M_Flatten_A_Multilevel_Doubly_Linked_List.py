"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
from typing import Optional
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def flatten_helper(node):
            current = node
            last = None
            while current:
                if current.child:
                    child = current.child
                    current.child = None
                    child_tail = flatten_helper(child)
                    next_node = current.next
                    current.next = child
                    child.prev = current
                    if child_tail:
                        child_tail.next = next_node
                        if next_node: next_node.prev = child_tail
                    last = child_tail if child_tail else current
                else: last = current
                current = current.next
            return last
        
        flatten_helper(head)
        return head