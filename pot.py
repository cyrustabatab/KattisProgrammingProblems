



def pot():


    n = int(input())

    s = 0
    for _ in range(n):

        number = input()

        power = int(number[-1])
        number = int(number[:-1])

        s += number**power


    print(s)




pot()

