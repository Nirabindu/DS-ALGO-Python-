
# Implementation of LinkedList Using Python

class Node:
    
    def __init__(self, value: any) -> None:
        
        """ Each Node contain values and next node address 
        """
        self.value = value
        self.next = None
        
    
class LinkedList:
    
    def __init__(self):
        
        self.head = None
        self.tail = None
        self.length = 0
    
    def print_list(self) -> None:
        """ This method used to print Elements from list
        Time-Complexity will O(n)
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def append(self, value: any):
        
        """This method used to add data in list from last
        There will be two condition 
        1. Appending in Empty List
        2. Appending a Non-Empty List
        
        as we are used to add data using tail pointer so time-complexity
        will O(1)
        i.e if we using loop to finding out the last node it will become
        O(n) Time-complexity
        
        """
        new_node = Node(value)
        
        # appending in empty list
        if self.head is None:
            self.head,self.tail = new_node, new_node
        # Appending in Non-Empty List
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True

    def pop(self):
        
        """This method used to remove items from the end of list
        There are 3 conditions need to check 
        1. pop from empty list
        2. only one elements in the list
        3. more then one elements
        and, Time Complexity will O(n)
        """
        # check for empty list
        if self.head is None:
            return None
        
        # check for Non Empty List
        # using two pointers
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre  = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        
        # now check for 1 value
        # if one value are there it already length -1 == 0
        if self.length == 0:
            self.head, self.tail = None, None
        return temp
        
    def prepend(self, value: any):
        
        """This methods used to add node from head
        there are 2 condition we needs to check 
        1. empty list
        2. Non- Empty-List
        and, The Time-Complexity will be O(1)
        """
        new_node = Node(value)
        # check for empty list
        if self.head is None:
            self.head,self.tail = new_node,new_node
        else:
            # for non empty list
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True
    
    def pop_first(self):
        """This method used to pop a node from from of the list
        Here need to check for 3 condition 
        1. Empty list
        2. Non Empty list
        3. one elements in the list
        
        time-complexity will be O(1)
        """
        
        if self.head is None:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1
        if self.length == 0:
            self.head, self.tail = None, None
        return temp
            
    def get(self, index: int):
        """This method used to get the value by using index
        
        condition that we need to check:
        1. the Index is correct, i.e non negative and > length
    
        Time-Complexity will O(n)
        """            
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index: int, value: any):
        """This method used to set the values in given Index position
        Time-Complexity will O(n)
        """ 
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index: int, value: any):
        """This method used to insert a node in given position 
        condition:
            1. Insert at front of the list - call prepend()
            2. Insert at end of the lost- call append 
            3. Insert middle/any where in the list
            Time Complexity is O(n)
        """
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next  = new_node
        self.length +=1
        return True
    
    def remove(self, index):
        """This method used to remove a node using index
        O(n)
        """
        
        if index < 0 or index >=self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        """This Method used to reverse the linkedList
        O(n) time complexity
        """
        temp = self.head
        self.head = self.tail
        self.tail = temp
        
        after = temp.next
        before = None
        
        for _ in range(self.length):
            
            # change the direction
            after = temp.next
            temp.next = before
            
            # swapping
            before = temp
            temp = after
            
            
# calling 
obj = LinkedList()

# appending
obj.append(1)
obj.append(2)
obj.append(3)
obj.append(4)
obj.append(5)
obj.print_list()
print('\n')
obj.pop()
obj.pop()
obj.print_list()
print('\n')
obj.prepend(0)
obj.prepend(-1)
obj.print_list()
print('\n')
obj.pop_first()
obj.pop_first()
obj.print_list()
print('\n')

print(obj.get(1).value)
print(obj.get(2).value)
print('\n')

obj.set_value(0,100)
obj.print_list()
print('\n')

obj.insert(1,500)
obj.print_list()
print('\n')

obj.remove(0)
obj.print_list()
print('\n')
obj.reverse()
obj.print_list()