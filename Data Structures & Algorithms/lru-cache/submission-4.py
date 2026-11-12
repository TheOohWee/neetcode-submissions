class ListNode:
    def __init__(self, key = 0, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left
        self.c = capacity
        self.d = {}

    def add(self, node):
        t = self.right.prev
        t.next = node
        node.prev = t
        node.next = self.right
        self.right.prev = node
    
    def remove(self, node):
        t = node.prev 
        a = node.next
        t.next = a
        a.prev = t

    def get(self, key: int) -> int:
        if key in self.d:
            self.remove(self.d[key])
            self.add(self.d[key])
            return self.d[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
        self.d[key] = ListNode(key, value)
        self.add(self.d[key])

        if len(self.d) > self.c:
            a = self.left.next
            self.remove(a)
            del self.d[a.key]
