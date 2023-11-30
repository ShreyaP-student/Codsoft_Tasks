def talkbot_response(user_input):
    # Define predefined rules and responses
    rules = {
        "hi": "Hello! How can I help you?",
        "how are you": "I'm a chatbot, I don't have feelings, but thanks for asking!",
        "bye": "Goodbye! Have a great day!",
        "what is your name": "I'm a chatbot. You can call me ChatGPT!",
        "what time is it": "I'm sorry, I don't have access to real-time information.",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "how old are you": "I don't have an age. I'm here to assist you!",
        "who created you": "I was created by a team of developers at OpenAI.",
        "thank you": "You're welcome! If you have more questions, feel free to ask.",
        "help": "Sure, I can assist you. What do you need help with?"
        # Add more rules and responses as needed
    }

    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if the user input matches any predefined rules
    for rule, response in rules.items():
        if rule in user_input:
            return response

    # If no match is found, provide a default response
    return "I'm not sure I understand. Can you rephrase or ask something else?"

# Simple interaction loop
print("Welcome! Ask me something or say 'bye' to exit.")
while True:
    user_query = input("You: ")
    if user_query.lower() == 'bye':
        print("Bot:", talkbot_response(user_query))
        break
    else:
        print("Bot:", talkbot_response(user_query))
