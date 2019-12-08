# 用两个栈实现队列
class MyQueue(object):
    def __init__(self):
        self.queue = []
        self.pop_queue = []

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        while len(self.queue) > 1:
            self.pop_queue.append(self.queue.pop())
        value = self.queue.pop()
        if self.pop_queue:
            while self.pop_queue:
                self.queue.append(self.pop_queue.pop())
        return value

    def is_empty(self):
        return not self.queue

    def __str__(self):
        return str(self.queue)


q = MyQueue()
for i in range(5):
    q.push(i)
print(q)
print(q.is_empty())
q.pop()
print(q)
