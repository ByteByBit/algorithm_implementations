import random
from timeit import default_timer as timer

from bogo import bogo_sort
from brick import brick_sort
from bubble import bubble_sort
from bucket import bucket_sort
from coctail import coctail_sort
from comb import comb_sort
from counting import counting_sort
from cycle import cycle_sort
from gnome import gnome_sort
from heap import heap_sort
from insertion import insertion_sort
from merge import merge_sort
from pigeonhole import pigeonhole_sort
from quick import quick_sort
from selection import selection_sort
from strand import strand_sort
from tim import tim_sort


def print_result(a_name: str, sorted_arr: list, elapsed: int):

    txt = '{algo_name}:\nSorted list: {s_list}\nTime (s): {elapsed}.\n' \
        '##########################################################################################' \
        .format(
                algo_name = a_name.capitalize(),
                s_list = ','.join(str(e) for e in sorted_arr),
                elapsed = elapsed)

    print(txt)


def timer_f(func, a:list):
    start = timer()

    res_tmp = func(a)

    end = timer()

    time_elapsed = 1000 * (end - start)

    print_result(a_name=func.__name__, sorted_arr=res_tmp, elapsed=time_elapsed)


if __name__ == '__main__':


    arr = list(range(60))
    random.shuffle(arr)
    
    # Bucket sort is mostly used for list of floats.
    bucket_list = [0.222, 0.333, 0.555, 0.444, 0.111, 0.232]
    # Counting sort is mostly used for 1 digit integers.
    counting_list = [9, 0, 0, 2, 1, 4, 4, 7, 9, 6, 7, 8, 5]

    print('Original list:\n {}'.format(','.join(str(e) for e in arr)))
    print('Bucket list:\n {}'.format(','.join(str(e) for e in bucket_list)))
    print('Counting list:\n {}'.format(','.join(str(e) for e in counting_list)))
    '''
    Bogo sort.
    '''
    # Limit the list to avoid recursion limit.
    timer_f(bogo_sort, a=arr[:5])

    '''
    Brick sort.
    '''
    timer_f(brick_sort, a=arr[:])

    '''
    Bubble sort.
    '''
    timer_f(bubble_sort, a=arr[:])

    '''
    Bucket sort.
    '''
    timer_f(bucket_sort, a=bucket_list[:])

    '''
    Coctail sort.
    '''
    timer_f(coctail_sort, a=arr[:])

    '''
    Comb sort.
    '''
    timer_f(comb_sort, a=arr[:])

    '''
    Counting sort.
    '''

    timer_f(counting_sort, a=counting_list[:])

    '''
    Cycle sort.
    '''
    timer_f(cycle_sort, a=arr[:])

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

    '''
    Strand sort.
    '''
    timer_f(strand_sort, a=arr[:])

    '''
    Tim sort.
    '''
    timer_f(tim_sort, a=arr[:])