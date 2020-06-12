# Non-growable buffer with a fixed size
# When the ring buffer is full and a new element is inserted
    # oldest element in the ring buffer is overwritten with the newest element 
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = list()

    def append(self, item):
        # for item in range(capacity)
        # or 
        # while len(storage) < capacity
        if item not in self.storage: 
            self.storage.append(item)
            return True
        else: 
            return False

    def get(self):
        return self.storage