import random

def random_integer(min, max):
    """
    Generates a random integer between min and max (both included).
   
    :param int min: minimum
    :param int max: maximum
    """
    return random.randint(min, max)


def random_operation():
    """
    Returns a random mathematical operation ('+', '-', '*').
    """
    return random.choice(['+', '-', '*'])


def evaluate_problem(number1, number2, operation):
    """
    Evaluates the problem and returns the both the string formatted version and the integer result.

    :param int number1: input number 1
    :param int number2: input number 2
    :param str operation: mathematical operation
    """
    problem = f"{number1} {operation} {number2}"
    if operation == '-': answer = number1 - number2
    elif operation == '+': answer = number1 + number2
    else: answer = number1 * number2
    return problem, answer

def main():
    """
    Run a new instance of Math Quiz Game
    """

    score = 0
    max_questions = 10

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(max_questions):
        # Generate random input numbers and operation
        number1 = random_integer(1, 10)
        number2 = random_integer(1, 5)
        operation = random_operation()

        # Calculate the result
        problem, answer = evaluate_problem(number1, number2, operation)
        print(f"\nQuestion: {problem}")

        # Let the user repeat the input until an integer was provided
        while True:
            try:
                useranswer = input("Your answer: ")
                useranswer = int(useranswer)
                break
            except ValueError:
                print(f"\nInvalid input, try again.")


        # Check if the user answered correctly
        if useranswer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    # User answered all questions
    print(f"\nGame over! Your score is: {score}/{max_questions}")

if __name__ == "__main__":
    main()
