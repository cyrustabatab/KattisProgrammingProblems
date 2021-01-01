


def is_harshad(n):
    
    original =n
    s = 0
    while n:
        s += n % 10
        n //= 10


    return original % s == 0



def harshad():


    n = int(input())



    while True:

        if is_harshad(n):
            print(n)
            break


        n += 1




harshad()
