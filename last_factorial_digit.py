


def last_factorial_digit():


    n = int(input())

    
    mapping = {1:1 ,2:2,3: 6,4: 4}
    for _ in range(n):
        number = int(input())

        if number in mapping:
            print(mapping[number])
        else:
            print(0)




last_factorial_digit()

