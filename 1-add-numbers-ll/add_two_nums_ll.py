# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        a1 = []
        a2 = []
        while l1 or l2:
            if l1:
                a1.append(l1.val)
                l1 = l1.next
            if l2:
                a2.append(l2.val)
                l2 = l2.next
        n1 = int(''.join([str(x) for x in a1]))
        n2 = int(''.join([str(x) for x in a2]))
        nsum = n1 + n2
        asum = []
        while nsum:
            asum.append(nsum % 10)
            nsum //= 10
        asum.reverse()
        lsum = ListNode(asum.pop())
        node = lsum
        while len(asum) > 0:
            node.next = ListNode(asum.pop())
            node = node.next
        return lsum

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val,)
    result = result.next
# 7 0 8