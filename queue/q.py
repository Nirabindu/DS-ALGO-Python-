
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Queue:
    
    def __init__(self):
        self.first  = None
        self.last = None
        self.length = 0
        
    def print_queue(self):
        
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def enqueue(self,value):
        # inserting from last
        new_node = Node(value)
        if self.first is None:
            self.first, self.last = new_node,new_node
        else:
            self.last.next = new_node
            self.last  = new_node
            
        self.length +=1
        
    def dequeue(self):
        # removing from first
        if self.first is None:
            return None
        
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        
        else:
            self.first = self.first.next
            temp.next = None
            
        self.length -=1
        return temp.value


qu = Queue()

qu.enqueue(34)
qu.enqueue(35)
qu.enqueue(36)
qu.print_queue()
print(qu.length)
print("dequeue")

print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())
qu.print_queue()
print(qu.length)
print(qu.first,qu.last)


                
        
            
        
        