#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    elif length == 2:
         print([0, 1])
         return
    else:
        fib = [ 0, 1]
        while len(fib) < length:
            fib.append(fib[-1]+ fib[-2])
        print(fib)
    # elif length == 2:
    #     print([0, 1])
    #     return
    pass