# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        numbers = []
        entries = [l1, l2]
        for entry in entries:
            digits = []
            while entry.next:
                digits.append(entry.val)
                entry = entry.next
            digits.append(entry.val)
            num = int(''.join([str(digit) for digit in reversed(digits)]))
            numbers.append(num)
        sum_of_numbers = sum(numbers)
        nodes = []
        for digit in reversed(str(sum_of_numbers)):
            nodes.append(ListNode(int(digit)))
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]
