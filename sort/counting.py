def counting_sort(a: list) -> list:
    """ 
    Counting sort algorithm.
    
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
    output = [0] * n

    # Count list.
    count = [0] * 10

    # Count each elem in the list and store it.
    for i in range(n):
        count[a[i]] += 1

    # Store the commulative count.
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each elem of the original list
    i = n - 1
    while i >= 0:
        output[count[a[i]] -1] = a[i]
        count[a[i]] -= 1
        i -= 1

    return output