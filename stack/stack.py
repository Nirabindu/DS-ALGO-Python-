
# Implementation of Stack


class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack:
    
    def __init__(self):
        self.top = None
        self.height = 0
    
    def print_stack(self):
        
        temp = self.top
        while temp is not None:
            
            print(temp.value)
            temp = temp.next
            
    def push(self, value):
        '''
        pushing in stack id O(1)
        
        '''
        
        # empty stack
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height +=1
        
    def pop(self):
        
        if self.top is None:
            return None
        temp = self.top
        if self.height == 1:
            self.top = None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -=1
        return temp.value
            
     

st = Stack()
st.print_stack()
st.push(2)
st.push(1)
st.print_stack()
print(st.height)
print("popping out")
print("poped Item is",st.pop())
st.print_stack()
print("height",st.height)
print("poped Item is",st.pop())
st.print_stack()
print("height",st.height)