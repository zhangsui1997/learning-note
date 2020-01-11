# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, pivot):
        stack = []
        # index = -1
        cur = head
        while cur:
            # if cur.val != pivot:
            #     index += 1
            stack.append(cur)
            cur = cur.next

        # 利用快排的partition思想 快慢指针
        less = -1
        more = len(stack)
        index = 0
        while index < more:
            if stack[index].val < pivot:
                less += 1
                stack[less], stack[index] = stack[index], stack[less]
                index += 1
            elif stack[index].val > pivot:
                more -= 1
                stack[more], stack[index] = stack[index], stack[more]
            else:
                index += 1

        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
        stack[-1].next = None
        return stack[0]


a = ListNode(9)
b = ListNode(0)
c = ListNode(4)
d = ListNode(5)
e = ListNode(1)
pivot = 5
a.next = b
b.next = c
c.next = d
d.next = e
solve = Solution()
p = solve.partition(a,1)

while p:
    print(p.val)
    p = p.next
