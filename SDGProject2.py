import random

# List of questions and correct answers
questions = [

    {
        "question": "In a rural village, farmers started using drought-resistant seeds and rainwater harvesting techniques.\n"
                    "Their crop yields have improved.\n"
                    "What is the main benefit of using drought-resistant seeds and rainwater harvesting in farming?\n"
                    "A) Increasing food production despite dry conditions.\n"
                    "B) Reducing the need for education.\n"
                    "C) Encouraging migration to cities.\n"
                    "D) Lowering food prices in urban markets.",
        "answer": "A"
    },
    {
        "question": "What is the main aim of the United Nations' Sustainable Development Goal 2: Zero Hunger?\n"
                    "A) Reduce the global population.\n"
                    "B) End hunger and achieve food security.\n"
                    "C) Promote space exploration.\n"
                    "D) Increase the use of fossil fuels.",
        "answer": "B"
    },
    {
        "question": "Paul lives in a rural village where many families don’t have enough to eat.\n"
                    "He starts a small community garden where neighbors can grow vegetables together and share the harvest.\n"
                    "How is Paul helping to support the goal of Zero Hunger?\n"
                    "A) By creating a business that only he profits from.\n"
                    "B) By encouraging food waste.\n"
                    "C) By increasing access to nutritious food for his community.\n"
                    "D) By banning all outside food.",
        "answer": "C"
    },
    {
        "question": "Which of the following is a key target of SDG 2: Zero Hunger?\n"
                    "A) Increase global fast food chains.\n"
                    "B) Ensure access to safe, nutritious food for all.\n"
                    "C) Reduce the number of farms.\n"
                    "D) Promote food advertising.",
        "answer": "B"
    },
    {
        "question": "John notices that his school throws away a lot of uneaten food every day.\n"
                    "He suggests starting a program to donate leftover food to a local shelter.\n"
                    "How does this idea support the Zero Hunger goal?\n"
                    "A) It helps reduce food waste and feed people in need.\n"
                    "B) It increases school food costs.\n"
                    "C) It encourages students to waste more food.\n"
                    "D) It makes the school cafeteria less popular.",
        "answer": "A"
    }
]

print("Welcome to the Zero Hunger Quiz, brought to you by SDG number 2: Zero Hunger!")
print("It is up to you, user, to give all the poor people all the food they need,")
print("Just by selecting the right answers, you can save lives.")
print("Type 'Play' to start the game or 'Quit' to exit. Your choice:")

choice = input("Enter your choice: ").strip().lower()

while choice != "quit":
    if choice == "play":
        points = 0
        donated_food = 0

        for i in range(len(questions)):
            print(f"\nQuestion {i + 1}:")
            print(questions[i]["question"])
            user_answer = input("Pick your answer (A/B/C/D): ").strip().upper()

            if user_answer == questions[i]["answer"]:
                print("Correct! You gained +100 points and donated 50% food to people in need!")
                points += 100
                donated_food += 50
            else:
                print("Incorrect! You lost -25 points.")
                points -= 25
                if points < 0:
                    points = 0
                    print(
                        "Game Over! You lost all your points and could not provide enough supplements. Better luck next time!")
                    break

        print("\n--- Quiz Completed, Your fate has been sealed ---")
        print(f"Your final score: {points} points")
        print(f"Food donated: {donated_food}%")
        if points > 0:
            print("Congratulations! You have successfully donated enough food to the people in need! What a Hero!")
        break

    else:
        print("Invalid choice. Please type 'Play' or 'Quit'.")
        choice = input("Enter your choice: ").strip().lower()

print("Au revoir!")