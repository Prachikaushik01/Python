#Create a program of displaying questions to the user like KBC.
#Use list datA type to store the questions and their correct answers

print("WELCOME TO FUNNY KBC")
print("Answer questions and become a CROREPATI!")
print("Let's see how intelligent you are!\n")

# List of questions
questions = [
    "1. What do we call a person who sleeps in class?",
    "2. What is the favourite food of a lazy person?",
    "3. What happens when you study one day before exams?",
    "4. Which animal says Meow?",
    "5. What is the national game of students during exams?"
]

# List of options
options = [
    ["A. Teacher", "B. Legend", "C. Principal", "D. Doctor"],
    ["A. Pizza", "B. Maggi", "C. Salad", "D. Fruits"],
    ["A. Success", "B. Panic", "C. Vacation", "D. Nothing"],
    ["A. Dog", "B. Cow", "C. Cat", "D. Lion"],
    ["A. Sleeping", "B. Cricket", "C. Studying", "D. Guessing"]
]

# List of correct answers
answers = ["B", "B", "B", "C", "D"]

# Prize money
prizes = [1000, 5000, 10000, 50000, 100000]

amount = 0

# Display questions
for i in range(len(questions)):

    print("\n" + questions[i])

    for option in options[i]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == answers[i]:
        amount = amount + prizes[i]
        print(" CORRECT! Wah! Kya dimaag hai!")
        print("You won Rs.", amount)

    else:
        print(" WRONG ANSWER!")
        print("Even Google is disappointed!")
        

print("GAME OVER!")
print("Your final winning amount is Rs.", amount)

if amount == 100000:
    print("CONGRATULATIONS! YOU ARE A CROREPATI!")
else:
    print("Better luck next time! ")

print("Thank you for playing FUNNY KBC!")
