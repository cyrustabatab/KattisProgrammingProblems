import math


def quick_estimates():

    n = int(input())

    base = 10
    for _ in range(n):

        estimate = int(input())

        if estimate == 0:
            print(1)
        else:
            digits_required = math.floor(math.log(estimate,10)) + 1


            print(digits_required)



quick_estimates()



        





