# LIFO

class Stack():
    def __init__(self):
        self.items =[]
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        self.items.pop()
        
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items
    

# s = Stack()
# s.push('A')
# print('Is Stack Empty: ' + str(s.is_empty()))
# s.push('B')
# s.push('C')
# s.pop()
# s.push('D')
# print('At the Peak: ' + s.peek())
# print('     Stack:      ')
# print(s.get_stack())