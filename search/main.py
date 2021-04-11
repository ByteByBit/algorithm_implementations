import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np
from threading import Thread
import queue

from binary import binary_search
from exponential import exponential_search
from interpolation import interpolation_search
from jump import jump_search
from linear import linear_search


def timer_f(func, a:list, r: int, x: int) -> None:
    '''
    Measure the time for the execution of a function. 
    
    Parameters
    ----------
    func : function
        The searching function.
    a : list
        Set of numbers to search in.
    r : int
        Length of the list.
    x : int
        The value we are looking for.
    '''

    start = timer()

    res_tmp = func(a, r, x)

    end = timer()
    res = {func.__name__: end - start}

    q.put(res)


def thread_manager(searching_funcs: list, r: int, x: int) -> None:
    ''' 
    Function to insert all sorting function into a thread.
    Parameters
    ----------
    searching_funcs : list
        The searching functions.
    a : list
        Set of numbers to search in.
    r : int
        Length of the list.
    x : int
        The value we are looking for.
    '''

    for f in searching_funcs:

        t = Thread(target=timer_f, args=(f, arr[:], r, x, ))
        t.daemon = True
        t.start()

def queue_manager(fun_length: int) -> dict:
    ''' 
    Function to retrieve data from qs, filled by the threads.
    Parameters
    ----------
    fun_length : int
        Length of the searching functions.
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
    plt.title('Searching algorithms time complexity (s)')
    plt.show()


if __name__ == '__main__':
    
    # Generate a random list
    arr = [x for x in range(0,30000)]
    
    # Algorithm list -> see readme.
    searching_funcs = [
        binary_search,
        exponential_search,
        interpolation_search,
        jump_search,
        linear_search
    ]

    # Queue -> see readme.
    q = queue.Queue()

    r = len(arr) - 1
    x = 5000

    # Send all function to a Thread.
    thread_manager(searching_funcs=searching_funcs, r=r, x=x)

    # Get results from the qs.
    results = queue_manager(fun_length=len(searching_funcs)-1)

    # Init and show chart.
    chart(data=results)