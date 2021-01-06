


def number_fun():


    n = int(input())


    for _ in range(n):
        number_1,number_2,number_3 = map(int,input().split())

    
        if (number_1 + number_2 == number_3) or (abs(number_1 - number_2) == number_3) or (number_1 * number_2 == number_3) or ((max(number_1,number_2)/min(number_1,number_2))== number_3):
            print("Possible")
        else:
            print("Impossible")



number_fun()
