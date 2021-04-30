import logging


def karatsuba(x: int, y: int) -> int:
    ''' Implementation of the Karatsuba multiplication algorithm. '''

    # When the numbers are small enough, just do the
    # default way.
    if x < 16 or y < 16:
        return x * y

    # Get bit half the length of the bigger number.
    n = max(x.bit_length(), y.bit_length()) // 2

    # Left shift, (2 ^ n) - 1
    mask = (1 << n) - 1

    # Right shift, x / 2 ^ n
    a, c = x >> n, y >> n

    # Bitwise and.
    b, d = x & mask, y & mask

    # A * C.
    part_1 = karatsuba(a, c)
    # B * D.
    part_2 = karatsuba(b, d)
    # (A+B) * (C+D) - A*C - B*D
    part_3 = karatsuba(a+b, c+d) - part_1 - part_2

    # ((AC * 2 ^ n) + (A+B) * (C+D) - AC - BD) * 2 ^ n ) + BD.
    return (((part_1 << n) + part_3) << n) + part_2


def main():

    # Some kinda large integer.
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627

    return karatsuba(x, y)


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    result = main()

    logging.info(f'The result is {result}')
