# Doubly Linked List
# pointing both side

class Node:
    
    def __init__(self, value: any):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    
    def __init__(self):
        
        self.head = None
        self.tail = None
        self.length = 0
    
    
    def print_list(self):
        
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head,self.tail = new_node, new_node
        
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
            
    def pop(self):
        """_summary_
        """
        if self.head is None:
            return None
        # here we need to return pop data for one node as well as multiple node 
        temp = self.tail
        if self.length ==1:
           self.head, self.tail = None, None
        
        else:
            
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
        
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head, self.tail = new_node, new_node
        else:
            new_node.next = self.head
            self.head.prev  = new_node
            self.head = new_node
        self.length +=1
        return True
            
    def pop_first(self):
        
        if self.head is None:
            return None
        temp = self.head
        if self.length == 1:
            self.head, self.tail = None, None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -=1
        return temp
        
    def get(self, index):

        # here we can apply the same as we use get for 
        # single linked list but we can optimize it here in doublyLinked-list
        
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        
        if index < self.length/2:
            
            for _ in range(index):
                print("inside for")
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
              
    def insert(self, index, value):
        # again we can implement the same code as single linked list here also
        
        if index < 0 or index > self.length:
            return None
        
        if index == 0:
            return self.prepend(value)
            
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before  = self.get(index-1)
        after = before.next
        
        new_node.next = after
        before.next = new_node
        new_node.prev = before
        after.prev = new_node
        self.length +=1
        return True

    def remove(self, index):
        
        if index < 0 or index >= self.length:
            return None
        if index == 0 :
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -=1
        return temp
        
        
        
     

        
        
            
        
        
ddl = DoublyLinkedList()
ddl.append(1)
ddl.append(2)
ddl.append(3)
ddl.append(4)
ddl.append(5)
ddl.append(6)
# print(ddl.get(1).value)

print("Inserting here")
ddl.insert(3,100)
ddl.print_list()

print("Removing Items")
ddl.remove(4)
ddl.print_list()


                
                
            
        
        
        
        

        
        
        
        