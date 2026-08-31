class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = self.right = ListNode(0, 0) # dummy nodes for quick pointer access
        self.left.next, self.right.prev = self.right, self.left


    def remove(self, node: ListNode):
        # removes node from the list
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode
    

    def insert(self, node: ListNode):
        # inserts node at the right end of the list
        prevNode = self.right.prev
        prevNode.next = self.right.prev = node
        node.prev, node.next = prevNode, self.right


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
