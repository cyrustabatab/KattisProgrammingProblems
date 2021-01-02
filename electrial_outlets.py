



def electric():


    n = int(input())

    for _ in range(n):
        s = 0
        k,*outlets = map(int,input().split())

        total_outlets = sum(outlets)
        s += total_outlets - (k - 1) # how to power other k - 1 power strips as well so lose k - 1 outlets due to those being plugged in 


        print(s)








        

electric()






