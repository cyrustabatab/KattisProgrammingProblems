import pdb


def skocimis():

    a,b,c = map(int,input().split())


    positions = [a,b,c]

    
    moves = 0
    while True:

        distance_1 = positions[1] - positions[0]

        distance_2 = positions[2] - positions[1]


        max_distance = max(distance_1,distance_2)


        if max_distance > 1:
            
            moves += 1
            if max_distance == distance_1:

                positions[2],positions[1] = positions[1],positions[0] + 1
            else:

                positions[0],positions[1] = positions[1],positions[1] + 1
        else:
            break




    print(moves)



skocimis()


# [5,6,9]
#[6,7,9]
#[7,8,9]




















