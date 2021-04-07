from insertion import insertion_sort


def bucket_sort(a: list) -> list:
    """ 
    Bucket sort algorithm.
    
    Parameters
    ----------
    a : list
        The list to sort.

    Returns
    -------
    list
        The sorted list.
    """

    arr = []
    slot_num = 10

    # Create buckets.
    for i in range(slot_num):
        arr.append([])

    # Fill buckets.
    for j in a:
        index_b = int(slot_num * j)          
        arr[index_b].append(j)

    # Insertion sort each bucket.
    for i in range(slot_num):
        arr[i] = insertion_sort(arr[i])

    k = 0
    # Insert the values back in order.
    for i in range(slot_num):
        for j in range(len(arr[i])):
            a[k] = arr[i][j]
            k += 1

    return a
