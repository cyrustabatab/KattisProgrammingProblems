



def odd():

    n = int(input())

    for i in range(1,n + 1):

        g = int(input())

        

        j = 0
        numbers = map(int,input().split())


        for number in numbers:
            j ^= number
    

        print(f"Case #{i}: {j}")




odd()





