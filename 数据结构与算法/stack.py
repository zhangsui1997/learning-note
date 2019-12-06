# 实现栈 并实现get_min()返回最小值,时间复杂度O(1)
class my_queue(object):
    def __init__(self, size):
        self.size = size
        self.queue = [] # 栈
        self.min_queue = [] # 最小栈

    def push(self, value):
        if len(self.queue) == self.size:
            raise IndexError
        self.queue.append(value)

        # 入栈时 如果小于等于小栈最后一个元素就也入最小栈
        if not self.min_queue:
            self.min_queue.append(value)
        elif self.min_queue[-1] >= value:
            self.min_queue.append(value)

    def pop(self):
        value = self.queue.pop(-1)
        if value == self.min_queue[0]:
            self.min_queue.pop(-1)
        return value

    def get_min(self):
        return self.min_queue[-1]


q = my_queue(5)
for i in range(4):
    q.push(i)
q.push(0)
print(q.queue, q.min_queue)
q.pop()
print(q.queue)
print(q.get_min())
