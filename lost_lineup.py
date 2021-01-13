




def lost():

    n = int(input())


    line = [None] * n

    line[0] = 1


    numbers = map(int,input().split())

    
    jimmy_position = 0
    for i,number in enumerate(numbers):
        i += 2
        line[jimmy_position +number + 1] = i
    
    
    
    for person in line:
        print(person,end=' ')



lost()
    









    




