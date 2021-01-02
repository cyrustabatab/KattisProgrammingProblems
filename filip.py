



def reverse_number(number):

    new_number = 0
    i = 2


    while number:
        new_number += (number % 10) * 10**i
        number //= 10
        i -= 1


    return new_number









def reverse_larger():


    number_1,number_2 = map(int,input().split())

    

    number_1 = reverse_number(number_1)
    number_2 = reverse_number(number_2)


    print(max(number_1,number_2))





reverse_larger()






