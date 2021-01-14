




def missing():


    n = int(input())

    
    previous = 0
    

    missing = False
    for _ in range(n):
        number = int(input())

        if number != previous + 1:

            missing = True
            j = previous + 1

            while j < number:
                print(j)
                j += 1


        previous = number
    
    
    if not missing:
        print('good job')


    
missing()











