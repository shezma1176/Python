import random

questions = [
    {
        "question": "Which animal was famously used by Hannibal to cross the Alps?",
        "options": ["Horse", "Elephant", "Camel", "Ox"],
        "answer": "Elephant"
    },
    {
        "question": "Which animal was considered sacred in Ancient Egypt?",
        "options": ["Dog", "Cat", "Horse", "Snake"],
        "answer": "Cat"
    },
    {
        "question": "Which animal carried messages during World War I?",
        "options": ["Dog", "Pigeon", "Horse", "Rabbit"],
        "answer": "Pigeon"
    },
    {
        "question": "What animal symbolized power in the Roman Empire?",
        "options": ["Lion", "Wolf", "Eagle", "Bear"],
        "answer": "Eagle"
    },
    {
        "question": "Which animal helped soldiers transport supplies in ancient deserts?",
        "options": ["Elephant", "Camel", "Donkey", "Horse"],
        "answer": "Camel"
    }
]

def start_quiz():
    print("\n🐾 Welcome to the History Animal Quiz! 📜")
    name = input("Enter your name: ")
    print(f"\nHello {name}! Let's test your history knowledge 🧠\n")

    score = 0
    random.shuffle(questions)

    for q in questions:
        print(q["question"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Your answer (1-4): "))
            if q["options"][choice - 1] == q["answer"]:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}\n")
        except:
            print("⚠ Invalid input! Skipping question.\n")

    print(f"🎉 Quiz Over, {name}!")
    print(f"📊 Your Score: {score}/{len(questions)}")

    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        start_quiz()
    else:
        print("👋 Thanks for playing! Have a great day!")

if __name__ == "__main__":
    start_quiz()