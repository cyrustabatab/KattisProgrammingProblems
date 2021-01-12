import math
from string import ascii_uppercase
import pdb


def racing():
    

    diameter = 60

    radius = diameter/2
    pi = 3.14
    circumference = 2 * pi * radius

    mod = 28

    distance_between_points = circumference/mod

    n = int(input())

    
    mapping = {}
    for i,c in enumerate(ascii_uppercase):
        mapping[c] = i


    mapping["'"] = 26
    mapping[' '] = 27

    

    speed = 15


    for _ in range(n):


        aphorism = input()

        seconds= 1 
        previous_character = aphorism[0] 
        for i in range(1,len(aphorism)):

            seconds += 1
            character = aphorism[i]

            value_1 = mapping[previous_character]
            value_2 = mapping[character]
            
            distance_1 = (value_1 - value_2) % mod
            distance_2 = (value_2 - value_1) % mod

            min_distance = min(distance_1,distance_2)


            total_distance_in_feet = min_distance * distance_between_points

            seconds += total_distance_in_feet / speed
            previous_character = character

        
        
        print(seconds)



racing()


            
















