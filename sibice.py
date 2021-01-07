import math



def sibice():


    n,width,height = map(int,input().split())
    

    
    diagonal = math.sqrt(width**2 + height**2)

    for _ in range(n):
        length = int(input())

        if length <= diagonal:
            print("DA")
        else:
            print("NE")




sibice()



















