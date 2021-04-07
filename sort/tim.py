MIN_MERGE = 32
def calc_min_run(run: int) -> int:
    ''' 
    Calculate min run.
    The value should be less or equal to a power of 2.

    Parameters
    ----------
    run : int
        The current run value.

    Returns
    -------
    int
        The new run.
    
    '''

    r = 0
    while run >= MIN_MERGE:

        r |= run & 1
        run >>= 1

    return run + r

def insertion_sort(a: list, left: int, right: int) -> None:
    ''' 
    Insertion sort the selected list slice.
    Parameters
    ----------
    a : list
        The list to sort.
    left : int
        Start index of the slice.
    right : int
        End index of the slice. 
    '''

    for i in range(left + 1, right + 1):

        j = i

        while j > left and a[j] < a[j - 1]:

            # Swap them.
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1

def merge(a: list, left: int, mid: int, right: int) -> None:
    ''' 
    Merge the selected list slices.
    Parameters
    ----------
    a : list
        The list to sort.
    left : int
        Start index of the slice.
    right : int
        End index of the slice. 
    '''

    left_len = mid - left + 1
    right_len = right - mid
    left_a, right_a = [], []

    for i in range(left_len):

        left_a.append(a[left + i])

    for i in range(right_len):

        right_a.append(a[mid + 1 + i])

    i, j, k = 0, 0, left

    while i < left_len and j < right_len:

        if left_a[i] <= right_a[j]:

            a[k] = left_a[i]
            i += 1

        else:

            a[k] = right_a[j]
            j += 1
        
        k += 1

    # Checking if any element is skipped.
    while i < len(left_a):
        a[k] = left_a[i]
        i += 1
        k += 1

    while j < len(right_a):
        a[k] = right_a[j]
        j += 1
        k += 1


def tim_sort(a: list) -> list:
    """ 
    Tim sort algorithm.
    
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

    min_run = calc_min_run(n)

    for start in range(0, n, min_run):

        end = min(start + min_run - 1, n - 1)
        insertion_sort(a, start, end)

    size = min_run

    while size < n:

        for left in range(0, n, 2 * size):

            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size -1), (n - 1))

            if mid < right:
                merge(a, left , mid, right)

        size = 2 * size

    return a