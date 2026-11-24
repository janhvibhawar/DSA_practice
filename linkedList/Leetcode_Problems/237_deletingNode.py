"""
LeetCode 237: Delete Node in a Linked List
Difficulty: Medium
Approach: Copy next node's value and bypass the next node.
Time Complexity: O(1)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next