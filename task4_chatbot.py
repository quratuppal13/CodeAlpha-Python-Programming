def rule_based_chatbot():
    print("--- CODEALPHA BASIC CHATBOT ---")
    print("Bot: Hello! I am a rule-based AI. How can I help you today?")
    print("(Type 'bye' anytime to close the chat)\n")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        # Checking predefined rules using if-elif-else
        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hi! Great to connect with you. What's on your mind?")
            
        elif "how are you" in user_input:
            print("Bot: I'm operating perfectly at full capacity! Thank you. How are you?")
            
        elif "your name" in user_input or "who are you" in user_input:
            print("Bot: I am the CodeAlpha Python Chatbot Assistant.")
            
        elif "bye" in user_input or "exit" in user_input:
            print("Bot: Goodbye! It was nice chatting with you. Have a great day ahead!")
            break
            
        else:
            print("Bot: I'm sorry, I am a basic chatbot. I can only understand simple greetings like 'Hi', 'How are you', or 'Bye'.")

# Launch the chatbot
if __name__ == "__main__":
    rule_based_chatbot()
