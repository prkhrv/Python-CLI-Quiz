def start_quiz(questions):
    score = 0
    for i in range(0, len(questions)):
        print(questions[i]["question"]+"\n")
        for j in range(1, 5):
            print(str(j)+" "+questions[i]["option"+str(j)])
            print()
        answer = int(input())
        print()
        if(answer > 0 and answer < 5):
            if(questions[i]["correct_answer"] == "option"+str(answer)):
                print("Correct Answer!!!\n")
                score = score + 1
            else:
                correct_answer = questions[i]["correct_answer"]
                print("Wrong!! The Correct Answer is {}".format(
                    questions[i][correct_answer]))
                print()
        else:
            print("Invalid Choice\n")
            continue

    print("Your Score is {}/{}".format(score,len(questions)))
