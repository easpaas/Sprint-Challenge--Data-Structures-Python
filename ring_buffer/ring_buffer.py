# Non-growable buffer with a fixed size
# When the ring buffer is full and a new element is inserted
    # oldest element in the ring buffer is overwritten with the newest element 
class RingBuffer:
    def __init__(self, capacity):
        self.buffer = []
        self.capacity = capacity

    def append(self, item):
        # before append check if length of buffer is equal to capacity?
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)
        else:
            self.buffer[0] = item

    def get(self):
        return self.buffer