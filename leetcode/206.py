# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        reversed = []
        
        p = head
        while p:
            reversed.insert(0, p.val)
            
        p = head
        i = 0
        
        while p:
            p.val = reversed[i]
            i += 1
            p.next = reversed[i+1]
            
        return head