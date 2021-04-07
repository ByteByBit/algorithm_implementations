def selection_sort(a: list) -> list:
    """ 
    Selection sort algorithm.
    
    Parameters
    ----------
    a : list
        The list to sort.

    Returns
    -------
    list
        The sorted list.
    """

    for i in range(len(a)):

        # Minimum elem of the remaining unsorted list.
        min_key = i

        for j in range(i+1, len(a)):

            if a[min_key] > a[j]:
                min_key = j

        # Swap the found smaller elem with the first elem.
        a[i], a[min_key] = a[min_key], a[i]

    
    return a