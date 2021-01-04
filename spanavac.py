



def spanavac():

    

    minutes_before = 45
    h,m = map(int,input().split())

    
    minutes = m - minutes_before


    if minutes < 0:

        minutes = 60 - abs(minutes)
        
        if h == 0:
            hour = 23
        else:
            hour = h -1
    else:
        hour = h


    print(hour,minutes)




spanavac()
































