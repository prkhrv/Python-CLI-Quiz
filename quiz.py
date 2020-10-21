from simple_chalk import chalk
from time import sleep

# Exception Handling here
class InputError(Exception):
    def __init__(self,value):
        self.value=value
def option_range(num):
    if(num>4 or num<1):
        raise InputError(chalk.yellow("Please enter a choice between 1 and 4"))

def start_quiz(questions):
    score = 0
    for i in range(0, len(questions)):
        print('--------------------------------------------------------')
        print(f'Q{i+1}) {questions[i]["question"]}\n'); sleep(0.2)
        
        for j in range(1, 5):
            print(f"({j}) {questions[i]['option'+str(j)]:30}", end='\t'); sleep(0.1)
            if not j%2: print()

        # flag for controlling the loop
        flag = False
        while(flag==False):
            try:
                answer = int(input("\nEnter your option number: ")); sleep(0.2)
                option_range(answer)
                sleep(0.4)
                flag = True
            except InputError as error:
                print(error)
                sleep(0.4)
            except ValueError:
                print(chalk.cyan('Invalid Choice\n'))
            
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
