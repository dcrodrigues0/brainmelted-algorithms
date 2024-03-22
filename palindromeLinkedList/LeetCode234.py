#  Leet Code 234. Palindrome Linked List

# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        
        arr = []
        while(head):
            arr.append(head.val)
            head = head.next
        return arr[::-1] == arr

solution = Solution()
palindromeTrue = ListNode(1, ListNode(2,ListNode(1)))
palindromeFalse = ListNode(1, ListNode(2,ListNode(2)))
print(solution.isPalindrome(palindromeTrue))
print(solution.isPalindrome(palindromeFalse))
# This solutions offers 282 ms of runtime.
