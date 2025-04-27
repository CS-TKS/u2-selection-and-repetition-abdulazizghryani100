import random

# the questions itself
questions = ["In a rural village, farmers started using drought-resistant seeds and rainwater harvesting techniques.\n Their crop yields has improved. \n What is the main benefit of using drought-resistant seeds and rainwater harvesting in farming?\nA)  Increasing food production despite dry conditions.\nB) Reducing the need for education.\nC) Encouraging migration to cities.\nD) Lowering food prices in urban markets.",
             "",
             ""]


        print("Welcome to the Zero Hunger Quiz, brought you by SDG number 2: Zero Hunger!")
        print("It is up to you, user, to give all the poor people all the food they need,")
        print("just by selecting one right answer, can save all.")
        print("Just choose 'Play' to start the game or 'Quit' to exit, its honestly your choice.")

        print(questions[0])
        #if (input == answer[0])

choice = input("Enter your choice: ").strip().lower()

while choice != "quit":
    if choice == "play":
        points = 0
        donated_food = 0

        for i in range(5):
            print("Question {i + 1}:")
            print(questions[i]["question"])
            user_answer = input("Pick answer (A/B/C/D): ").strip().upper()

            if user_answer == questions[i]["answer"]:
                print("Correct! You gained +100 points + Donated 50% of food to the people in need!")
                points += 100
                donated_food += 50
            else:
                print("Incorrect! You lost -25 points.")
                points -= 25
                if points < 0:
                    points = 0
                    print(
                        "Game Over! You lost all your points, and did not give enough supplements to the people in need, Better luck next time!")
                    break


        print("--- Quiz Completed, Your fate has been seeled ---")
        print("Your final score: {points} points")
        print("Food donated: {donated_food}%")
        print("Congratulations! You have successfully donated enough supplements to the people in need! What a Hero!")
        break

    else:
        print("Invalid choice. Please type 'Play' or 'Quit'.")
        choice = input("Enter your choice: ").strip().lower()

print("Au Revior!")