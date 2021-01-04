



def shattered_cake():



    width_of_cake = int(input())

    number_of_pieces = int(input())

    
    area = 0
    for _ in range(number_of_pieces):

        width_of_piece,length_of_piece = map(int,input().split())
        
        area_of_piece = width_of_piece * length_of_piece


        area += area_of_piece




    length_of_cake = area / width_of_cake


    print(int(length_of_cake))



shattered_cake()







        













