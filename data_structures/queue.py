# Python implementation of a FIFO queue.


class Fifo:
    def __init__(self):
        self.queue = []

    def __str__(self):
        """
        Allows printing of the queue
        """
        return str(self.queue)

    def enqueue(self, item):
        """
        Adds an items to the end of the queue
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Removes the first item from the queue and returns it
        """

        item = self.queue[0]
        self.queue = self.queue[1:]
        return item


x = Fifo()
x.enqueue(1)
x.enqueue("zorp")
x.enqueue(123)
x.enqueue((9, 4, 2))
x.enqueue([1, 2, 3])
x.enqueue(0)
print(x)

x.dequeue()
x.dequeue()
print(x)
