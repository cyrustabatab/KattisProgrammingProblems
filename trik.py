




def trik():



    s = input()

    
    starting_cup = 1
    cups = [starting_cup,2,3]
    for c in s:
        if c == 'A':
            cups[0],cups[1] = cups[1],cups[0]
        elif c == 'B':
            cups[1],cups[2] = cups[2],cups[1]
        else:
            cups[0],cups[2] = cups[2],cups[0]
    


    print(cups.index(starting_cup) + 1)



trik()

