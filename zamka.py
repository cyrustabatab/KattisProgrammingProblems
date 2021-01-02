

def sum_of_digits(number):


    s = 0

    while number:
        s += number % 10
        number //= 10

    return s


def zamka():


    L = int(input())
    D = int(input())
    X = int(input())

    
    minimum_found = False
    for number in range(L,D + 1):
        

        if sum_of_digits(number) == X:
            if not minimum_found:
                minimum_found = True
                minimum = number
            maximum= number
    


    print(minimum)
    print(maximum)



zamka()









