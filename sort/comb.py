def get_gap(gap: int) -> int:
    """ 
    Calculate the next gap, by multiplying the current
    one with 1.3. 
    
    Parameters
    ----------
    gap : int
        Current gap.

    Returns
    -------
    int
        The next gap.
    """

    # Decrease gap by 1.3
    gap = (gap * 10) // 13
    if gap < 1:
        return 1
    
    return gap

def comb_sort(a: list) -> list:
    """ 
    Comb sort algorithm.
    
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
    gap = n

    swapped = True

    while gap != 1 or swapped:

        gap = get_gap(gap=gap)

        swapped = False

        for i in range(n-gap):

            if a[i] > a[i + gap]:
                # Swap them.
                a[i], a[i + gap] = a[i + gap], a[i]
                swapped = True

    return a