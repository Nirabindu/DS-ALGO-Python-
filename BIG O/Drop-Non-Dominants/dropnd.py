def print_items(items):
    
    # n^2
    for item in range(items):
        
        for item2 in range(items):
            print(item2)
            
    # n times
    # non dominants loop can be discard calculating complexity
    for k in range(items):
        print(k)
        
    
    # so O(n^2 + n(non dominant)) = O(n^2)