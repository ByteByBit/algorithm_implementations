def insertion_sort(a: list) -> list:
    """ 
    Insertion sort algorithm.
    
    Parameters
    ----------
    a : list
        Set of numbers to search in.

    Returns
    -------
    list
        The sorted list.
    """
    
    # Start iteration from second elem.
    for i in range(1, len(a)):

        key = a[i]
        j = i-1

        # Go backwards and swap the elems 
        # if the elem is bigger than the key.
        while j>=0 and key < a[j]:

            a[j+1] = a[j]
            j -= 1

        a[j+1] = key

    return a
