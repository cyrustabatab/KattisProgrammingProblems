




def reverse():


    n = int(input())

    stack = []
    for _ in range(n):
        number = int(input())
        stack.append(number)
    


    while stack:
        print(stack.pop())




reverse()
