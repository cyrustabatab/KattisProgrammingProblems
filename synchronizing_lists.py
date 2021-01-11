



def synchronizing_lists():


    n = None


    while n != 0:

        n = int(input())

        
        first_list , second_list = [],[]
        lists = [first_list,second_list]

        for i in range(2):
            l = lists[i]
            for _ in range(n):
                number = int(input())
                l.append(number)

        


        sorted_first_list = sorted(first_list)

        indexes = {number: i for i,number in enumerate(sorted_first_list)}
        second_list.sort()

        for number in first_list:
            index = indexes[number]

            print(second_list[index])


        print()





synchronizing_lists()





            



# 10 67 68 28
# 55 73 10 6










