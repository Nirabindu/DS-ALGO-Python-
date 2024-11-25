'''
all the node smaller then root present in left side and all
the nodes greater then root present in right side 

Time- Complexity


no of nodes in a full binary tree  = 2^n-1  n= level
searching a node is O(n) worst case(if the tree gradually on one side lke linked-list) but we treat it as o(log n)

so, lookup() , insert() , remove() O(log n)

inserting better for linked list coz it O(1)

'''


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    
class BinarySearchTree:
    
    def __init__(self):
        # same like head in linked list
        self.root = None

    def insert_node(self, value):
        
        new_node = Node(value)
        
        # check for empty tree
        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root
        while True:
            if new_node.value == temp.value:
                # bst should not have any duplicate values
                return False
            
            if new_node.value > temp.value:
                
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp  = temp.left
                
    def contains(self, value):
        
        temp = self.root

       
        while temp:          
            if temp.value == value:
                return True
            
            if value > temp.value:
                temp = temp.right
            else:
                temp = temp.left
        return False

            
                
            
                

bst = BinarySearchTree()
bst.insert_node(2)
bst.insert_node(1)
bst.insert_node(3)
# bst.insert_node(3)
print(bst.contains(2))

# print(bst.root.value,'\n', bst.root.left.value,'\n',bst.root.right.value)
