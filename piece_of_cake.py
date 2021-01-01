


def piece_of_cake():

    length_of_side,h,v = map(int,input().split())


    thickness = 4


    width_1,width_2 = length_of_side - v,v
    length_1,length_2 = length_of_side -h,h

    
    maximum = float("-inf")
    for width in (width_1,width_2):
        for length in (length_1,length_2):
            maximum = max(width * length,maximum)



    biggest_volume = maximum * thickness
    print(biggest_volume)








piece_of_cake()









