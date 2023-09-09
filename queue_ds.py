# First
# In
# First
# Out

class Queue(object):
    def __init__(self, limit=10):
        self.queue = []
        self.front = None
        self.rear = None
        self.limit = 10
        self.size = 0

    def __str__(self) -> str:
        return ' '.join([str(i) for i in self.queue])

    def enqueue(self, data):
        if self.size >= self.limit:
            return -1
        
        else:
            self.queue.append(data)

        if self.front is None:
            self.rear = self.front = 0
        else:
            self.rear = self.size
        
        self.size += 1

    def isEmpty(self):
        return self.size <= 0

    def dequeue(self):
        if self.isEmpty():
            return -1

        else:
            self.queue.pop(0)
            self.size -= 1

            if self.size == 0:
                self.front = self.rear = 0

            else:
                self.rear = self.size -1
    
    def getSize(self):
        return self.size


if __name__ == "__main__":
    Queue1 = Queue()
    Queue1.enqueue(10)
    Queue1.enqueue(15)
    Queue1.enqueue(19)
    Queue1.enqueue(7**2)
    Queue1.enqueue(3**10)
    print(Queue1)
    print(f'Size {Queue1.getSize()}')
    Queue1.dequeue()
    
    