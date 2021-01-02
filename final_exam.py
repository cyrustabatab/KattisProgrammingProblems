






def final_exam():

    number_of_questions = int(input())

    
    num_correct = 0

    previous_score = None
    for _ in range(number_of_questions):
        score = input()

        num_correct += (score == previous_score)

        previous_score = score





    print(num_correct)



final_exam()









