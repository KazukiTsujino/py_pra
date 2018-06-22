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

word_list = input("Enter words,please.")
unreverse = Stack()
for c in word_list:
    unreverse.push(c)
reverse = ""

while unreverse.size():
    reverse += unreverse.pop()
print(reverse)
 