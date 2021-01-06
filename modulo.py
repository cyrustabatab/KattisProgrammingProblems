


def modulo():

    n= 10

    
    unique = set()
    for _ in range(n):

        number = int(input())

        
        mod = number % 42
        unique.add(mod)


    print(len(unique))


modulo()










