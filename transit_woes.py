




def transit():

    s,t,n = map(int,input().split())

    
    walk_times = list(map(int,input().split()))
    bus_ride_times = map(int,input().split())
    bus_intervals = map(int,input().split())


    time = s


    for walk_time,bus_ride_time,bus_interval in zip(walk_times,bus_ride_times,bus_intervals):
        time += walk_time
        if time % bus_interval != 0:
            time = (time // bus_interval + 1) * bus_interval
        time += bus_ride_time

    
    time += walk_times[-1]

    if time <= t:
        print('yes')
    else:
        print('no')




transit()











