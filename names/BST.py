from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the value to the root's value to determine which direction
        if value < self.value:
            # go left
            # check if there is a left node
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            # go right
            # check if there is a right node
            if self.right: 
                self.right.insert(value)
            else: 
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self == None:
            return False
        if target == self.value:
            return True
        # essentially need to repeat insert() functionality
        if target < self.value: 
            # go left 
            # check if there is a left node
            if self.left == None:
                return False
            else: 
                # Recursive call checks the self.left.value
                return self.left.contains(target)
        else: 
            # go right
            # check if there is a left node
            if self.right == None:
                return False
            else:
                # Recursive call checks the self.right.value 
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right: 
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
