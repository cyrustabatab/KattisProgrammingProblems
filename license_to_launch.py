



def license():

    n = int(input())



    numbers = map(int,input().split())

    
    min_junk = float("inf")
    min_day = None
    for i,number in enumerate(numbers):
        if number < min_junk:
            min_junk = number
            min_day = i


    print(min_day)


license()












