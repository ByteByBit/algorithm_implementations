def merge_sort(a: list) -> list:
    """ 
    Merge sort algorithm.
    
    Parameters
    ----------
    a : list
        Set of numbers to search in.

    Returns
    -------
    list
        The sorted list.

    """

    if len(a) > 1:
 
        # Define the middle of the list.
        mid = len(a)//2
 
        # Define left half of the list.
        left = a[:mid]
 
        # Define right half of the list.
        right = a[mid:]
 
        # Sort the left part.
        merge_sort(left)
 
        # Sort the right part.
        merge_sort(right)
 
        i = j = k = 0
 
        # Sort the two sub lists.
        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1

            k += 1
 
        # Checking if any element is skipped.
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
        
    return a