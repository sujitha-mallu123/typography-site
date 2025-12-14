print("Welcome to Healthcare Chatbot")

while True:
    user = input("You: ")
    if user.lower() in ["fever", "cold", "headache"]:
        print("Bot: Please drink warm water and take rest. If symptoms persist, consult a doctor.")
    elif user.lower() == "exit":
        print("Bot: Take care! Stay healthy.")
        break
    else:
        print("Bot: Sorry, I can only give basic health advice. Consult a doctor for detailed help.")
