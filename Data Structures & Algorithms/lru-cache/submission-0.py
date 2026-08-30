

class LRUCache:

    # We can maintain a map as well as a linked list for creating an LRU cache.

    # A map provides O(1) retrieval and updates, but how do we know when to evict a cached pair?

    # We can use a linked list, which represents the order of pairs inserted into the cache.
    # A newly cached pair goes into the front of the list. The older pairs are towards the end.

    # When the length of the list is greater than the cache capacity, we remove from the end of the list.
    # We also remove the corresponding map pair.

    class ListNode:
        def __init__(self, key, value, next=None, prev=None):
            self.key = key
            self.value = value
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.maxCapacity = capacity
        self.cacheMap = {}

        self.left = self.ListNode(0, 0)
        self.right = self.ListNode(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: ListNode):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def insert(self, node: ListNode):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key not in self.cacheMap:
            return -1
        
        self.remove(self.cacheMap[key])
        self.insert(self.cacheMap[key])
        return self.cacheMap[key].value
    

    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])
        self.cacheMap[key] = self.ListNode(key, value)
        self.insert(self.cacheMap[key])

        if len(self.cacheMap) > self.maxCapacity:
            lru = self.left.next
            self.remove(lru)
            del self.cacheMap[lru.key]