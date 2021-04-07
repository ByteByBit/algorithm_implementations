def pigeonhole_sort(a: list) -> list: 
    """ 
    Pigeonhole sort algorithm.
    
    Parameters
    ----------
    a : list
        The list to sort.

    Returns
    -------
    list
        The sorted list.

    """

    lowest = min(a) 
    highest = max(a) 
    # Size of the pigeonholes.
    size = highest - lowest + 1
  
    holes = [0] * size 
  
    # Fill the pigeonholes. 
    for x in a: 
        holes[x - lowest] += 1
  
    i = 0
    # Insert the elems back to the original list. 
    for count in range(size): 

        while holes[count] > 0:

            holes[count] -= 1
            a[i] = count + lowest 
            i += 1
    
    return a
              