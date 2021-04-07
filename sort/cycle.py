def cycle_sort(a: list) -> list:
    """ 
    Cycle sort algorithm.
    
    Parameters
    ----------
    a : list
        The list to sort.

    Returns
    -------
    list
        The sorted list.
    """

    n = len(a)
    count = n - 1
    for cycle_start in range(count):

        item = a[cycle_start]
        pos = cycle_start

        # Find a place for the item.
        for i in range(cycle_start + 1, n):
            if a[i] < item:
                pos += 1

        # Item is in the right place, move on.
        if pos == cycle_start:
            continue
            
        # If there are any duplicate, put after them.
        while item == a[pos]:

            pos += 1

        # Swap them.
        a[pos], item = item, a[pos]

        # Rotate the rest of the cycle.
        while pos != cycle_start:

            pos = cycle_start

            # Find where to put the item.
            for i in range(cycle_start + 1, n):

                if a[i] < item:
                    pos += 1

            # If there are any duplicate, put after them.
            while item == a[pos]:

                pos += 1
            
            # Swap them.
            a[pos], item = item, a[pos]
        
    return a