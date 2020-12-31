




def qaly():


    n = int(input())

    
    quality = 0
    for _ in range(n):

        n1,n2 = map(float,input().split())


        quality += n1 * n2


    print(quality)



qaly()








