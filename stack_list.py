class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last_index = len(self.items) - 1
        return self.items[last_index]
    
    def size(self):
        return len(self.items)

lis = Stack()
reversed_list = []
for i in range(1,6):
    lis.push(i)

for i in range(5):
    reversed_list.append(lis.pop())
print(reversed_list)