from timeit import default_timer as timer

from bogo import bogo_sort
from bubble import bubble_sort
from bucket import bucket_sort
from counting import counting_sort
from gnome import gnome_sort
from heap import heap_sort
from insertion import insertion_sort
from merge import merge_sort
from pigeonhole import pigeonhole_sort
from quick import quick_sort
from selection import selection_sort


def print_result(a_name: str, original_arr: list, sorted_arr: list, elapsed: int):

    txt = '{algo_name}:\n Original list: {o_list}, sorted list: {s_list}, time (s): {elapsed}.\n' \
        '##########################################################################################' \
        .format(
                algo_name = a_name,
                o_list = ','.join(str(e) for e in original_arr),
                s_list = ','.join(str(e) for e in sorted_arr),
                elapsed = elapsed)

    print(txt)

def timer_f(func, a:list):
    start = timer()

    res_tmp = func(a)

    end = timer()

    time_elapsed = 1000 * (end - start)

    print_result(a_name=func.__name__, original_arr=arr, sorted_arr=res_tmp, elapsed=time_elapsed)


if __name__ == '__main__':

    arr = [12, 11, 13, 5, 6, 44, 17, 19, 87] 

    '''
    Bogo sort.
    '''
    # Limit the list to avoid recursion limit.
    timer_f(bogo_sort, a=arr[:5])

    '''
    Bubble sort.
    '''
    timer_f(bubble_sort, a=arr[:])

    '''
    Bucket sort.
    '''
    # Bucket sort is mostly used for list of floats.
    arr1 = [0.222, 0.333, 0.555, 0.444, 0.111, 0.232]
    timer_f(bucket_sort, a=arr1)

    '''
    Counting sort.
    '''
    arr1 = [9, 0, 0, 2, 1, 4, 4, 7, 9, 6, 7, 8, 5]
    timer_f(counting_sort, a=arr1[:])

    '''
    Gnome sort.
    '''
    timer_f(gnome_sort, a=arr[:])

    '''
    Heap sort.
    '''
    timer_f(heap_sort, a=arr[:])

    '''
    Insertion sort.
    '''
    timer_f(insertion_sort, a=arr[:])

    '''
    Merge sort.
    '''
    timer_f(merge_sort, a=arr[:])

    '''
    Pigeonhole sort.
    '''
    timer_f(pigeonhole_sort, a=arr[:])

    '''
    Quick sort.
    '''
    timer_f(quick_sort, a=arr[:])

    '''
    Selection sort.
    '''
    timer_f(selection_sort, a=arr[:])
