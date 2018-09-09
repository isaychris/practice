# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#   Input: head = [4,5,1,9], node = 1
#   output: [4,5,1,9]

class Solution:        
    def deleteNode(self, node):
        if not node:
            return
        
        node.val = node.next.val
        node.next = node.next.next