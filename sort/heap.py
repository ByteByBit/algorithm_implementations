def heapify(a: list, n: int, i: int) -> list:
    """ 
    Heapify the given list.
    
    Parameters
    ----------
    a : list
        Set of numbers to search in.
    n : int 
        Lenght of the list.
    i : int
        Root candidate.

    Returns
    -------
    list 
        A heapified list.
    """

    largest = i # Root.
    left = 2 * i + 1    
    right = 2 * i + 2
  
    # If left child exists and larger than root.
    if left < n and a[i] < a[left]: 
        largest = left
  
    # If right child exists and larger than root.
    if right < n and a[largest] < a[right]: 
        largest = right
  
    # If root is not the largest.
    if largest != i: 
        a[i], a[largest] = a[largest], a[i] 

        # Heapify the root. 
        heapify(a, n, largest) 

    return a
  

def max_heap(a: list, i: int, n:  int) -> list:
    """ 
    Build max heap (recursive).
    
    Parameters
    ----------
    a : list
        Set of numbers to search in.
    i : int
        Iteration count.
    n : int  
        Half of the list minus 1.

    Returns
    -------
    list
        Max heaped list.
    """

    if i >= 0:
        i -= 1
        a = heapify(a, n, i) 
        max_heap(a, i, n)
    
    return a


def heap_sort(a: list) -> list: 
    """ 
    Heap sort algorithm.
    
    Parameters
    ----------
    a : list
        Set of numbers to search in.

    Returns
    -------
    list
        A formatted string of the sorted list and the
        iteration count.
    """
    n = len(a) 
    # Build max heap.
    a = max_heap(a, n//2 - 1, n)

    # One by one extract elements 
    for i in range(n-1, 0, -1): 

        a[i], a[0] = a[0], a[i] 
        a = heapify(a, i, 0) 

    return a





