# Non-growable buffer with a fixed size
# When the ring buffer is full and a new element is inserted
    # oldest element in the ring buffer is overwritten with the newest element 
from Doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.buffer = DoublyLinkedList()
        self.capacity = capacity
        self.current = None

    def append(self, item):
        # buffer not at capacity 
        if len(self.buffer) < self.capacity:
            self.buffer.add_to_tail(item)
            self.current = self.buffer.head
        else:
        # buffer is at capacity
            oldest_value = self.buffer.head
            self.buffer.remove_from_head()
            self.buffer.add_to_tail(item)

            if oldest_value == self.current:
                self.current = self.buffer.tail

    def get(self):
        # empty list to store values for ring_buffer
        temp_list = []

        if not self.buffer.length:
            return None

        # store the current item
        starting_node = self.current
        # add the current item to the list
        temp_list.append(starting_node.value)

        if starting_node.next:
            next_node = starting_node.next
        else:
            next_node = self.buffer.head

        # iterate over list finding the next_node 
        while next_node is not starting_node:
            temp_list.append(next_node.value)

            if next_node.next:
                next_node = next_node.next
            else:
                next_node = self.buffer.head

        return temp_list