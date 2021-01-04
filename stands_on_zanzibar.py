




def turtle_saver():


    n = int(input())


    for _ in range(n):


        numbers = map(int,input().split())

        
        previous_number = 1

        imported_turtles = 0
        for number in numbers:
            
            twice_previous_number = 2 * previous_number
            if number > twice_previous_number:
                imported_turtles += number - twice_previous_number

            previous_number = number



        print(imported_turtles)
    





turtle_saver()



















