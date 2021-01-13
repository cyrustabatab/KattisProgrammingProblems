




def mixed():
    





    numerator,denominator = map(int,input().split())

    while numerator != 0 and denominator != 0:

        whole_number = numerator//denominator

        remainder = numerator % denominator
        
        
        print(f"{whole_number} {remainder} / {denominator}")

        numerator,denominator = map(int,input().split())





mixed()



