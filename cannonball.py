import math




def cannonball():


    n = int(input())


    for _ in range(n):
        v0,theta,x1,h1,h2 = map(float,input().split())

        time_to_wall = x1/(v0 * math.cos(theta * (math.pi / 180)))

        g = 9.81
        y_position_at_wall = v0 * time_to_wall * math.sin(theta * (math.pi /180)) - 0.5 * g * time_to_wall**2


        safe =  h1 + 1 <= y_position_at_wall <= h2 - 1

        print('Safe' if safe else 'Not Safe')





if __name__ == "__main__":
    
    cannonball()






