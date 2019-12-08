# 实现栈 并实现get_min()返回最小值,时间复杂度O(1)
class MyStack(object):
    def __init__(self, size):
        self.size = size
        self.stack = []  # 栈
        self.min_stack = []  # 最小栈

    def push(self, value):
        if len(self.stack) == self.size:
            raise IndexError
        self.stack.append(value)

        # 入栈时 如果小于等于小栈最后一个元素就也入最小栈
        if not self.min_stack:
            self.min_stack.append(value)
        elif self.min_stack[-1] >= value:
            self.min_stack.append(value)

    def pop(self):
        value = self.stack.pop(-1)
        if value == self.min_stack[0]:
            self.min_stack.pop(-1)
        return value

    def get_min(self):
        return self.min_stack[-1]

    def __str__(self):
        return str(self.stack)


q = MyStack(5)
for i in range(4):
    q.push(i)
q.push(0)
print(q)
