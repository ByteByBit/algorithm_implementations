from timeit import default_timer as timer

from binary import binary_search
from exponential import exponential_search
from interpolation import interpolation_search
from jump import jump_search
from linear import linear_search


def print_result(a_name: str, searched_elem: list, elapsed: int, index: int):

    txt = '{algo_name}:\n searched elem: {searched_elem}, index: {index}, time (s): {elapsed}.\n' \
        '##########################################################################################' \
        .format(
                algo_name = a_name,
                searched_elem = searched_elem,
                index=index,
                elapsed = elapsed)

    print(txt)

def timer_f(func, a:list, r: int, x: int):
    start = timer()

    res_tmp = func(a=a, r=r, x=x)

    end = timer()

    time_elapsed = 1000 * (end - start)

    print_result(a_name=func.__name__, searched_elem=x, elapsed=time_elapsed, index=res_tmp)


if __name__ == '__main__':
    '''

    '''

    
    arr = list(range(60))
    
    print('Original list:\n {}'.format(','.join(str(e) for e in arr)))
    r = len(arr) - 1
    x = 59

    '''
    Binary search.
    '''
    timer_f(binary_search, a=arr, r=r, x=x)

    '''
    Exponential search.
    '''
    timer_f(exponential_search, a=arr, r=r, x=x)

    '''
    Interpolation search.
    '''
    timer_f(interpolation_search, a=arr, r=r, x=x)

    '''
    Jump search.
    '''
    timer_f(jump_search, a=arr, r=r+1, x=x)

    '''
    Linear search.
    '''
    timer_f(linear_search, a=arr, r=r+1, x=x)

