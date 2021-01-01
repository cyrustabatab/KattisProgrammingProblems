



def heart_rate():

    n = int(input())




    for _ in range(n):

        b,p = map(float,input().split())


        calculated_bpm = (60 *b /p)

        error = 60 / p



        print(f"{calculated_bpm - error:.4f} {calculated_bpm:.4f} {calculated_bpm + error:.4f}")



heart_rate()

