# Python-CLI-Quiz

A CLI Python Quiz App which throws 5 random questions to the Player and the Player has to answer them to Test his General Knowledge.

## :keyboard: To Start the Quiz
```python
:~$ python3 main.py
```
or simply
```
python main.py

```
To Add the Quiz in your Script, simply just Fork the Repo and import start_quiz

```python
from quiz import start_quiz
```
And Pass The Questions with it

```python
start_quiz(questions)
```
#### Question JSON Format

```
{
    "questions":
    [
      {
        "question": "What is the Capital of Uttar Pradesh?",
        "option1": "Kanpur",
        "option2": "Lucknow",
        "option3": "Noida",
        "option4": "Varanasi",
        "correct_answer": "option2"
      }
    ]
 }
```
#### :warning: Upcoming Changes

* Integration with the QUICK QUIZ API 


#### PRs will only be accepted from the assigned Person Only

#### Please do leave a :star: to support the Repo !!! 
