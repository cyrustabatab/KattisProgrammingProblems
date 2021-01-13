


def line():

    n = int(input())

    
    
    first_name = input()
    second_name = input()

    if first_name > second_name:
        decreasing = True
    else:
        decreasing = False

    
    previous_name = second_name
    for _ in range(n -2):
        name = input()


        if decreasing:
            if name > previous_name:
                print('NEITHER')
                break
        else:
            if name < previous_name:
                print('NEITHER')
                break
    else:
        if decreasing:
            print('DECREASING')
        else:
            print('INCREASING')
        






line()




