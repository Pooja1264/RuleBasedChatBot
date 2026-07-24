import datetime
import random

print("=" * 50)
print("Welcome to Rule-Based AI Chatbot")
print("Type 'help' to see available commands.")
print("Type 'bye' to exit.")
print("=" * 50)

jokes = [
    "Why do programmers prefer Python? Because it's easy to read!",
    "Why did the computer get cold? It forgot to close Windows.",
    "Debugging: Being the detective in a crime movie where you're also the criminal."
]

quotes = [
    "Success comes from consistent practice.",
    "Never stop learning.",
    "Every expert was once a beginner.",
    "Believe in yourself and keep coding!"
]

while True:
    user = input("\nYou: ").lower().strip()

    if user in ["hi", "hello", "hey", "good morning", "good evening"]:
        print("Bot: Hello! 😊 How can I help you today?")

    elif user == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user == "your name":
        print("Bot: My name is RuleBot.")

    elif user == "what is ai":
        print("Bot: AI (Artificial Intelligence) enables machines to perform tasks that normally require human intelligence.")

    elif user == "what is python":
        print("Bot: Python is a powerful programming language used in AI, Data Science, Web Development, and Automation.")

    elif user == "time":
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        print("Bot: Current Time:", current_time)

    elif user == "date":
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's Date:", current_date)

    elif user == "joke":
        print("Bot:", random.choice(jokes))

    elif user == "quote":
        print("Bot:", random.choice(quotes))

    elif user == "calculator":
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+ - * /): ")
            num2 = float(input("Enter second number: "))

            if op == "+":
                print("Result:", num1 + num2)
            elif op == "-":
                print("Result:", num1 - num2)
            elif op == "*":
                print("Result:", num1 * num2)
            elif op == "/":
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Cannot divide by zero.")
            else:
                print("Invalid operator.")
        except:
            print("Invalid input.")

    elif user == "help":
        print("\nAvailable Commands:")
        print("- hi / hello / hey")
        print("- how are you")
        print("- your name")
        print("- what is ai")
        print("- what is python")
        print("- date")
        print("- time")
        print("- joke")
        print("- quote")
        print("- calculator")
        print("- help")
        print("- bye")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! 👋 Have a great day!")
        break

    else:
        print("Bot: Sorry, I don't understand that. Type 'help' to see available commands.")
import datetime
import random

print("=" * 50)
print("Welcome to Rule-Based AI Chatbot")
print("Type 'help' to see available commands.")
print("Type 'bye' to exit.")
print("=" * 50)

jokes = [
    "Why do programmers prefer Python? Because it's easy to read!",
    "Why did the computer get cold? It forgot to close Windows.",
    "Debugging: Being the detective in a crime movie where you're also the criminal."
]

quotes = [
    "Success comes from consistent practice.",
    "Never stop learning.",
    "Every expert was once a beginner.",
    "Believe in yourself and keep coding!"
]

while True:
    user = input("\nYou: ").lower().strip()

    if user in ["hi", "hello", "hey", "good morning", "good evening"]:
        print("Bot: Hello! 😊 How can I help you today?")

    elif user == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user == "your name":
        print("Bot: My name is RuleBot.")

    elif user == "what is ai":
        print("Bot: AI (Artificial Intelligence) enables machines to perform tasks that normally require human intelligence.")

    elif user == "what is python":
        print("Bot: Python is a powerful programming language used in AI, Data Science, Web Development, and Automation.")

    elif user == "time":
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        print("Bot: Current Time:", current_time)

    elif user == "date":
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's Date:", current_date)

    elif user == "joke":
        print("Bot:", random.choice(jokes))

    elif user == "quote":
        print("Bot:", random.choice(quotes))

    elif user == "calculator":
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+ - * /): ")
            num2 = float(input("Enter second number: "))

            if op == "+":
                print("Result:", num1 + num2)
            elif op == "-":
                print("Result:", num1 - num2)
            elif op == "*":
                print("Result:", num1 * num2)
            elif op == "/":
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Cannot divide by zero.")
            else:
                print("Invalid operator.")
        except:
            print("Invalid input.")

    elif user == "help":
        print("\nAvailable Commands:")
        print("- hi / hello / hey")
        print("- how are you")
        print("- your name")
        print("- what is ai")
        print("- what is python")
        print("- date")
        print("- time")
        print("- joke")
        print("- quote")
        print("- calculator")
        print("- help")
        print("- bye")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! 👋 Have a great day!")
        break

    else:
        print("Bot: Sorry, I don't understand that. Type 'help' to see available commands.")