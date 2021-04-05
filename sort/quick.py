def quick_sort(a: list) -> list:
    """ 
    Quick sort algorithm.
    
    Parameters
    ----------
    a : list
        Set of numbers to search in.

    Returns
    -------
    list
        The sorted list.

    """

    less = []
    equal = []
    greater = []

    if len(a) > 1:

        pivot = a[0]

        for x in a:

            # Compare the list values one by one and
            # store in sub lists respectively to it's value.
            if x < pivot:
                less.append(x)

            elif x == pivot:
                equal.append(x)

            elif x > pivot:
                greater.append(x)

        # Sort the sub lists.
        return quick_sort(less) + equal + quick_sort(greater) 

     
    return a
