







def cudovisite():


    rows,cols = map(int,input().split())

    
    matrix = []
    for _ in range(rows):
        column = input()
        row = []
        for c in column:
            row.append(c)
        matrix.append(row)

    
    

    squashed_cars = {i: 0 for i in range(5)}
    
    start_row = 0
    step = 2
    for row in range(rows - 1):
        for col in range(cols -1):
            count = 0
            for i in range(2):
                for j in range(2):
                    value = matrix[row + i][col + j]
                    if value == '#':
                        break
                    elif value == 'X':
                        count += 1
                else:
                    continue
                break
            else:
                squashed_cars[count] += 1

        

    for value in squashed_cars.values():
        print(value)






cudovisite()
            


            














