import math
import pdb


def reversed_binary_numbers():

    n = int(input())

    
    base = 2
    bits = math.floor(math.log(n,base)) + 1
    reversed_n = 0

    end = bits - 1
    while n:
        bit = n & 1
        n >>= 1
        if bit:
            reversed_n += (base**end)

        end -= 1



    print(reversed_n)



reversed_binary_numbers()
