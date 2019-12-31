# Python implementation of a stack


class Stack:
    """
    Python implementation of a stack. AKA: FILO Queue.
    It's possible to force a particular use of a list to mimic the actions of
    a stack.
    """

    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, item):
        """
        Adds an item to the stack.
        """
        self.stack = [item] + self.stack

    def pop(self):
        """
        Removes and returns the top item from the stack.
        """

        item = self.stack[0]
        self.stack = self.stack[1:]
        return item

    def search(self, item):
        """
        A VERY naive version of a search. Searches through the stack and
        returns where in the stack the item is. Only finds the first location.
        This search has a worst case runtime of O(n) if the item was the first
        thing added to the stack.
        """
        for i in range(0, len(self.stack)):
            if self.stack[i] == item:
                return i
        return None


x = Stack()
x.push("First!")
x.push(1)
x.push(-32)
x.push([1, 2, 3, 4, 5])
print(x)

# Pop from the stack, should give us the most recently added
y = x.pop()
print(y)

# Get the index of 1, should be 1 after the pop operation
y = x.search(1)
print(y)
