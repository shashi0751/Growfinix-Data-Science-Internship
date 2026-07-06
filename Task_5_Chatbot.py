print("🤖 Welcome to the Travel Chatbot!")

while True:
    user = input("\nYou: ").lower()

    if user == "hello":
        print("Bot: Hello! How can I help you?")
    elif user == "hi":
        print("Bot: Hi! Nice to meet you.")
    elif user == "packages":
        print("Bot: We offer Goa, Manali, Kerala and Jaipur tour packages.")
    elif user == "price":
        print("Bot: Prices start from ₹15,000.")
    elif user == "contact":
        print("Bot: You can contact us at +91-9876543210.")
    elif user == "bye":
        print("Bot: Thank you! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I didn't understand. Try saying hello, packages, price, contact or bye.")