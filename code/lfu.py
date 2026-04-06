class DLLNode:
    def __init__(self, key, val):
        # Cache entry data
        self.key = key
        self.val = val
        # Every new key starts with frequency 1
        self.freq = 1
        # Pointers for doubly linked list
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        # Number of real nodes in this frequency bucket
        self.size = 0
        # Dummy head/tail make add/remove O(1) and clean
        self.head = DLLNode(0, 0)
        self.tail = DLLNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node):
        # Add right after head => most recently used in this frequency bucket
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove_node(self, node):
        # Remove node from its current position in O(1)
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curSize = 0
        # Smallest frequency currently present in cache
        self.minFrequency = 0
        # key -> node (direct access)
        self.cache = {}
        # frequency -> doubly linked list of nodes with that frequency
        self.freqMap = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Accessing a key increases its frequency
        node = self.cache[key]
        self.updateNode(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            # Existing key: update value and treat as access (freq++)
            node = self.cache[key]
            node.val = value
            self.updateNode(node)
            return

        # New key path
        self.curSize += 1

        if self.curSize > self.capacity:
            # Cache full: remove LFU node
            # Tie-break: remove LRU within minFrequency list (tail.prev)
            minList = self.freqMap[self.minFrequency]
            lruNode = minList.tail.prev
            minList.remove_node(lruNode)
            del self.cache[lruNode.key]
            self.curSize -= 1

        # New key always starts at frequency 1
        self.minFrequency = 1
        newNode = DLLNode(key, value)
        freqList = self.freqMap.get(1, DoublyLinkedList())
        freqList.add_node(newNode)
        self.freqMap[1] = freqList
        self.cache[key] = newNode

    def updateNode(self, node):
        # Remove from old frequency list
        freq = node.freq
        curList = self.freqMap[freq]
        curList.remove_node(node)

        # If old minFrequency list becomes empty, bump minFrequency
        if freq == self.minFrequency and curList.size == 0:
            self.minFrequency += 1

        # Move node to next frequency list
        node.freq += 1
        newList = self.freqMap.get(node.freq, DoublyLinkedList())
        newList.add_node(node)
        self.freqMap[node.freq] = newList