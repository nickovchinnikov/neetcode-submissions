class DLL:
    def __init__(self, key=None, val=None, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()

        self.tail = DLL()
        self.head = DLL()
        # tail <-> head
        self.head.nxt = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
        return node
    
    def insert(self, node):
        prev = self.tail.prev

        prev.nxt = node
        node.prev = prev
        node.nxt = self.tail

        self.tail.prev = node

        return node
    
    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        node = self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if not node:
            node = self.insert(DLL(key, value))
            self.cache[key] = node
        else:
            node.val = value
            self.remove(node)
            self.insert(node)
        
        if len(self.cache) > self.capacity:
            lru = self.head.nxt
            self.remove(lru)
            del self.cache[lru.key]


