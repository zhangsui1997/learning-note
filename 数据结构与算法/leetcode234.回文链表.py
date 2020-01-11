# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        quick, slow = head, head

        while quick.next and quick.next.next:
            slow = slow.next
            quick = quick.next.next
        mid = slow  # 记录下中点位置 方便后面在逆序回原链表

        # 翻转后面的链表
        pre = self.reverse_list(slow)
        end = pre

        # 首位开始对比
        while pre and head:
            if pre.val != head.val:
                # 反转回原样
                self.reverse_list(end)
                return False
            pre = pre.next
            head = head.next
        # 反转回原样
        self.reverse_list(end)
        return True

    def reverse_list(self, head):
        cur = head
        pre = None
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre


a = ListNode(1)
b = ListNode(1)
c = ListNode(2)
a.next = b
b.next = c

cw = Solution()
print(cw.isPalindrome(a))

print(c.next)
