


def tais():

    n = int(input())

    

    previous_time = None

    area = 0


    for _ in range(n):

        time,glucose = map(float,input().split())


        if previous_time is not None:
            height= time - previous_time
            area += (height * (previous_glucose + glucose)) / 2000


        previous_glucose,previous_time = glucose,time


    
    print(area)


tais()









            










        







