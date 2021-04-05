def bubble_sort(a: list) -> list:
    """ 
    Bubble sort algorithm.
    
    Parameters
    ----------
    a : list
        Set of numbers to search in.

    Returns
    -------
    list
        The sorted list.
    """

    n = len(a)

    for i in range(n):

        swapped = False

        for j in range(0, n-i-1):

            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True

        

        if swapped == False:
            return a  
