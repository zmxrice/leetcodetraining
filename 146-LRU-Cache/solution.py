class DoubleLinkedList(object):
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.pre = None
        self.next = None

class LRUCache(object):
    def moveToFront(self, cur):
        if cur.pre:
            cur.pre.next = cur.next
            if cur.next:
                cur.next.pre = cur.pre

        if not cur is self.head:
            cur.pre = None
            cur.next = self.head
            if self.head:
                self.head.pre = cur
            self.head = cur

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :rtype: int
        """
        if not key in self.cache:
            return -1
        cur = self.cache[key]
        if cur is self.tail and cur.pre:
            self.tail = cur.pre
        self.moveToFront(cur)
        return cur.val


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        cur = None
        if key in self.cache:
            cur = self.cache[key]
            cur.val = value
            if cur is self.tail and cur.pre:
                self.tail = cur.pre
            self.moveToFront(cur)
        else:
            cur = DoubleLinkedList(key, value)
            self.cache[key] = cur
            self.moveToFront(cur)
            if len(self.cache) == 1:
                self.head = self.tail = cur
            if len(self.cache) > self.capacity:
                self.cache.pop(self.tail.key)
                if self.tail.pre:
                    self.tail.pre.next = self.tail
                    self.tail = self.tail.pre