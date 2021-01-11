





def symmetric():




    set_number = 1
    n = int(input())
    while n != 0:
        

        print(f"SET {set_number}")
        stack= []
        for i in range(n):

            
            name = input()
            if i % 2 == 1:
                stack.append(name)
            else:
                print(name)

            


        while stack:
            name = stack.pop()
            print(name)


        set_number += 1

        n = int(input())


    
        

symmetric()
