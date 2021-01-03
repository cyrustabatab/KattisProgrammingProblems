import math



def star_arrangement():


    s = int(input())
    
    print(f"{s}:")

    for i in range(2,math.ceil(s/2) + 1):

        if (s - i) % (2 * i - 1) == 0 or (s % (2 * i - 1)) == 0:
            print(f"{i},{i - 1}")


        if s % i == 0:
            print(f"{i},{i}")

    



star_arrangement()

