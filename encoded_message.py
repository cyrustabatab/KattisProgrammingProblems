import math




def decode():


    n = int(input())

    

    for _ in range(n):


        parts = []
        message = input()
        square_side= int(math.sqrt(len(message)))


        end = square_side - 1
        
        for i in range(end,-1,-1):
            characters = []
            for j in range(square_side):
                character = message[i + square_side * j]
                characters.append(character)


            parts.append(''.join(characters))
        

    

        decoded_message = ''.join(parts)


        print(decoded_message)


decode()






















