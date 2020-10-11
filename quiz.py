from simple_chalk import chalk
from time import sleep

def start_quiz(questions):
    score = 0
    for i in range(0, len(questions)):
        print('--------------------------------------------------------')
        print(f'Q{i+1}) {questions[i]["question"]}\n'); sleep(0.3)
        
        for j in range(1, 5):
            print(f"({j}) {questions[i]['option'+str(j)]:30}", end='\t'); sleep(0.2)
            if not j%2: print()
        
        while True:
            try:
                answer = int(input("\nEnter your option number: ")); sleep(0.3)
                if not 0<answer<5:
                    print(chalk.yellow("Please enter a choice between 1 and 4\n")); sleep(0.4)
                else:
                    break
            except ValueError:
                print(chalk.cyan('Invalid Choice\n')); sleep(0.4)
            
        print()
        if(questions[i]["correct_answer"] == "option"+str(answer)):
            print(chalk.green("Correct Answer!!!\n")); sleep(0.4)
            score = score + 1
        else:
            correct_answer = questions[i]["correct_answer"]
            print(chalk.red(f"Wrong!! The Correct Answer is {questions[i][correct_answer]}")); sleep(0.4)
            print()
        
        print('--------------------------------------------------------\n\n')
        
    print(chalk.yellow(f"Your Score is {score}/{len(questions)}"))
