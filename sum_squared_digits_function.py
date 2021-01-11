



def calculate_ssd(base,number):
    

    s = 'ABCDEF'

    values = {c: 10 + i for i,c in enumerate(s)} 

    ssd = 0 
    while number:

        result = number % base

        if result in values:
            value = values[result]
        else:
            value = result

        
        ssd += value**2


        number //= base

    
    return ssd






def ssd():


    n = int(input())


    
    for _ in range(n):
        
        i,base,number = map(int,input().split())
        result = calculate_ssd(base,number)

        print(f"{i} {result}")





ssd()



