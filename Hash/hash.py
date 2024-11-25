
# hash is one way, dic is consider as Hash table in python
# Hash is Deterministic - getting value that is Deterministic

# Hash collision happened when there are values already in an address
# sol^n - 1. until found an empty address called Linear Probing(open addressing)
# soln -2 or we can use separate chaining of linkedlist create linked list if more than one hash in same address
# and work only when we have more then one key values in same address

# a consideration always take len == Prime numbers of address from starting 0 to avoid collision by giving Random ness
# so size  = 7 is o,1,2,3,4,5,6
class HashTable:
    
    # size = 7 is default size
    def __init__(self,size = 7):
        self.data_map = [None] * size
    

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            # ord(letter) give assici value of it and * 23 is a prime number we can use any 
            # prime number here
            # and divide by 7 given any number betn 0 to 6
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i , val in enumerate(self.data_map):
            print(i,": ", val)
    
    def set_item(self,key, value):
        index = self.__hash(key) 
        if self.data_map[index] == None:
            self.data_map[index] = []
        # if already having a value in same address simply append
        self.data_map[index].append([key,value])
    
    def get_item(self,key):
        index = self.__hash(key)
        
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

        
        




hash = HashTable()
# hash.print_table()   
hash.set_item('name','Nirabindu')
hash.set_item('age','14')
hash.set_item('country','India')
# hash.print_table() 
print(hash.get_item('age'))