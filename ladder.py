import math





def ladder():


    height,angle = map(int,input().split())

    
    length = height / (math.sin(angle * math.pi/180))


    print(math.ceil(length))





ladder()



