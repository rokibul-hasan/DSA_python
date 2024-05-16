def linear_search(arr,target):
    """ 
    Perform a linear search on the given list to find the target value.
    
    Parameters:
    arr (list): the list to search through.
    target ( any ) : the value to search for.
    
    Returns:
    int: The index of the target value if found, otherwise -1. 
    """
    
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
    
    
list = [10,20,30,40,50]
target_value = 30

result = linear_search(list,target_value)
if result != -1:
    print(f"Target value found at index {result}")
else:
    print("Target value not found")