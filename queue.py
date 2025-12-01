class Queue:
    def __init__(self): 
        self.items = []
    
    def is_empty(self):
        if len(self.items) == 0:
            empty = True
        else:
            empty = False
        return empty
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.items.pop(0)
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.items[0]
    
    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)