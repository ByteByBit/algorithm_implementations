import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np
from threading import Thread
import queue
import time

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


def timer_f(func, a:list) -> None:
    '''
    Measure the time for the execution of a function. 
    
    Parameters
    ----------
    func : function
        The sorting function.
    a : list
        A list to sort.
    '''

    start = timer()

    res_tmp = func(a)

    end = timer()
    res = {func.__name__: end - start}

    q.put(res)


def thread_manager(sorting_funcs: list) -> None:
    ''' 
    Function to insert all sorting function into a thread.

    Parameters
    ----------
    sorting_funcs : list
        The sorting functions.
    '''

    for f in sorting_funcs:

        t = Thread(target=timer_f, args=(f, arr[:], ))
        t.daemon = True
        t.start()


def queue_manager(fun_length: int) -> dict:
    ''' 
    Function to retrieve data from qs, filled by the threads.

    Parameters
    ----------
    fun_length : int
        Length of the sorting functions.
    '''

    results = {}
    count = 0
    while True:
        res = q.get()
        results.update(res)

        if count == fun_length:
            break
        
        count += 1

    return results


def chart(data: dict) -> None:
    ''' 
    Initialize and display matplotlib chart.

    Parameters
    ----------
    data : int
        Ex. { function_name: 0.003 }.

    '''

    plt.style.use('ggplot')
    keys = results.keys()
    vals = results.values()
    x_pos = [i for i, _ in enumerate(keys)]

    plt.bar(x_pos, vals)

    plt.xticks(x_pos, keys)
    plt.title('Sorting algorithms time complexity (s)')
    plt.show()


if __name__ == '__main__':


    # Generate a random list
    arr = random.sample(range(0, 3000), 100)

    # Algorithm list -> see readme.
    sorting_funcs = [
        # bogo_sort,
        brick_sort,
        bubble_sort,
        # bucket_sort,
        coctail_sort,
        comb_sort,
        # counting_sort,
        cycle_sort,
        heap_sort,
        insertion_sort,
        merge_sort,
        pigeonhole_sort,
        quick_sort,
        selection_sort,
        strand_sort,
        tim_sort
    ]

    # Queue -> see readme.
    q = queue.Queue()

    # Send all function to a Thread.
    thread_manager(sorting_funcs=sorting_funcs)

    # Get results from the qs.
    results = queue_manager(fun_length=len(sorting_funcs)-1)

    # Init and show chart.
    chart(data=results)