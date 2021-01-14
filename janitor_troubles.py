import math





def maximum():


    s1,s2,s3,s4 = map(int,input().split())


    s = s1 + s2 + s3 + s4

    s/= 2


    area= math.sqrt((s - s1) * (s - s2) * (s - s3) * (s - s4))

    print(area)


maximum()







