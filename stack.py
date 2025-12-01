class Stack:
    def __init__(self, _items):
        self._items = []
    
    def is_empty(self):
        if len(self._items) == 0:
            empty = True
        else:
            empty = False
        return empty
    
    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop item.")
            return None
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
            return None
        return self._items[-1]

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)