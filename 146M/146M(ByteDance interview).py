from collections import OrderedDict

class DLL:
    def __init__(self):
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insertHead(self, node):
        headNext = self.head.next
        headNext.prev = node
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        self.size += 1

    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1

    def removeTail(self):
        tail = self.tail.prev
        self.removeNode(tail)
        return tail

class ListNode:

    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.freq = 1
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.dll = DLL()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.dll.removeNode(node)
            self.dll.insertHead(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:  # similar to get()
            node = self.cache[key]
            self.dll.removeNode(node)
            node.val = value
            self.dll.insertHead(node) # replace the value len(dic)
            # self.cache[key] = node # shallow copy, no need to update in purpose
        else:
            if len(self.cache) >= self.capacity:
                tail = self.dll.removeTail()
                del self.cache[tail.key]
            node = ListNode(key, value)
            self.dll.insertHead(node)
            self.cache[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LRUCache(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            value = None

        return value

    def set(self, key, value):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
                self.cache[key] = value
            else:
                self.cache[key] = value