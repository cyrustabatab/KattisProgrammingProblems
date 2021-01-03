




def tarifa():


    X = int(input())


    n = int(input())

    
    
    extra_megabytes = 0
    for _ in range(n):
        P = int(input())
        megabytes_available = X + extra_megabytes
        extra_megabytes = megabytes_available - P
    



    print(X + extra_megabytes)
    


tarifa()    




