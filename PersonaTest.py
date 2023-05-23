def run_avenger_quiz():
    # Define the questions
    questions = [
        "What is your favorite color?\n(a) Red\n(b) Blue\n(c) Green\n(d) Black\n",
        "What is your preferred superpower?\n(a) Super strength\n(b) Flight\n(c) Mind control\n(d) Stealth\n",
        "What is your ideal weapon of choice?\n(a) Hammer\n(b) Shield\n(c) Bow and arrow\n(d) Iron suit\n",
        "How would you describe your personality?\n(a) Brave\n(b) Noble\n(c) Intelligent\n(d) Mysterious\n",
    ]

    # Define the Avenger results
    avenger_results = {
        "Iron Man": 0,
        "Captain America": 0,
        "Thor": 0,
        "Black Widow": 0,
    }

    # Ask the questions and store the answers
    answers = []
    for question in questions:
        answer = input(question)
        answers.append(answer.lower())  # Convert the answer to lowercase for easier comparison

    # Calculate the result based on the answers
    for answer in answers:
        if answer == 'a':
            avenger_results["Iron Man"] += 1
        elif answer == 'b':
            avenger_results["Captain America"] += 1
        elif answer == 'c':
            avenger_results["Thor"] += 1
        elif answer == 'd':
            avenger_results["Black Widow"] += 1

    # Determine the Avenger with the highest score
    avenger = max(avenger_results, key=avenger_results.get)

    # Print the result
    print("Based on your answers, you are", avenger)

# Run the quiz
run_avenger_quiz()
