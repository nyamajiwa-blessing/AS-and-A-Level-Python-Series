class QueueADT:
    
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)


q1 = QueueADT()
fruits = ["orange","apple","banana","pineapple"]

for fruit in fruits:
    q1.enqueue(fruit)

print(q1.size())

