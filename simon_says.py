





def simon():


    n = int(input())

    
    starting_index_for_valid_instruction = 11

    start = "Simon says"
    for _ in range(n):

        instruction = input()



        if instruction.startswith(start):
            print(instruction[starting_index_for_valid_instruction:])






simon()






