


def speed():





    n = int(input())
    while n != -1:


        previous_time = 0
        total_miles = 0
        for _ in range(n):
            mph,time = map(int,input().split())

            elapsed_time = time - previous_time

            miles = mph * elapsed_time
            total_miles += miles
            previous_time = time
        
        print(f"{total_miles} miles")
        n = int(input())
        

        

speed()




