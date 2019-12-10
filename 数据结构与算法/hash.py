'''
设计一种结构，在该结构中有如下三个功能： insert(key)：将某个key加入到该结构，做到不重复加入。
delete(key)：将原本在结构中的某个key移除。
getRandom()： 等概率随机返回结构中的任何一个key。
【要求】 Insert、delete和getRandom方法的时间复杂度都是 O(1)
'''


class RandomHash(object):
    def __init__(self):
        self.random = {}
        self.reverse_random = {}
        self.index = 0

    def insert(self, key):
        self.index += 1
        self.random[key] = self.index
        self.reverse_random[self.index] = key

    def get_random(self):
        import random
        return self.reverse_random[random.randrange(1,self.index+1)]

    def delete(self, key):
        # 删除 替代 index-1
        pass