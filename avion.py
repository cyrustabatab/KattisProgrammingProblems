


def avion():


    n = 5

    target = 'FBI'
    count = 0
    for i in range(1,n + 1):
        word = input()
        if target in word:
            print(i,end=' ')
            count += 1

    


    if count == 0:
        print("HE GOT AWAY!")




avion() 







