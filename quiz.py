def start_quiz(questions):
    score = 0
    for index, question in enumerate(questions):
        print(question["question"] + "\n")
        for j in range(1, 5):
            print(str(j) + " " + question["option" + str(j)], '\n')
        answer = int(input())
        print()
        if 5 > answer > 0:
            if question["correct_answer"] == "option" + str(answer):
                print("Correct Answer!!!\n")
                score += 1
            else:
                correct_answer = question["correct_answer"]
                print("Wrong!! The Correct Answer is {}".format(question[correct_answer]), '\n')
        else:
            print("Invalid Choice\n")

    print("Your Score is {}/{}".format(score, len(questions)))
