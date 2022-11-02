"""
Module for experimenting with lower and upper bounds.

Unlike in the BED functionality, where we need to search for a lower bound in
a list of features, here we only concern ourselves with lists of integers.
"""


def lower_bound(x: list[int], v: int) -> int:
    """Get the index of the lower bound of v in x.

    If all values in x are smaller than v, return len(x).
    """
    lower_bound_index = None 
    start = 0    #Starting point
    end = len(x) - 1     #Ending point 
    while start <= end:
        middle = (start + end)//2    #middle point 
        
        if x[middle] == v:
            lower_bound_index = middle
            end = middle - 1 # is there any v occurrance before?
        elif x[middle] > v:
            end = middle - 1    
        else:
            start = middle + 1
            
    if lower_bound_index is None:
        return len(x)
    return lower_bound_index



def upper_bound(x: list[int], v: int) -> int:
    """Get the index of the upper bound of v in x.

    If all values in x are smaller than v, return len(x).
    """
    bound_index = None 
    start = 0    #Starting point
    end = len(x)-1      #Ending point 
    while start <= end:
      
        middle = (start + end)//2    #middle point 
       
        if x[middle] == v:
            bound_index = middle
            start = middle + 1 # is there any v occurrance after?
        elif x[middle] > v:
            end = middle - 1    
        else:
            start = middle + 1
            
    if bound_index is None:
        return len(x)
    return bound_index

