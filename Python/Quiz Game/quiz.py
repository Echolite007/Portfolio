# Main function
def main():
    
    questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
    }

    options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
            ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
            ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
            ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]
    new_game(questions, options)

    while play_again() == True: 
        new_game(questions, options)

# Function to start new game 
def new_game(questions, options):
    guesses = [] 
    correct_guesses = 0
    question_num = 1

    for question in questions:
        print("----------------------------------------------")
        print(question)
        for option in options[question_num - 1]:
            print(option)
        guess = input("Answer (A) (B) (C) (D): ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(question), guess) # passing answer and guess to check_answer function
        question_num += 1

    display_score(correct_guesses, guesses, questions)

# Function to check answer 
def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Incorrect")
        return 0

# Function to display score
def display_score(correct_guesses, guesses, questions):
    print("-----ANSWERS-----")
    for guess in guesses:
        print(f"Your Answers: {guess}")
    for i in questions:
        print(f"Correct Answer: {questions.get(i)}")

    score = int((correct_guesses / len(questions)) * 100)

    print(f"SCORE: {str(score)}%")

# Function to play again
def play_again():
    response = input("Do you want to play again? (yes/no) ").lower()

    if response == "yes": 
        return True
    else: 
        print("Thanks for playing!")
        return False
    
# Call main
main()