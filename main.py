# Command Line Chat bot

import time

# Function to greet the user
def greet_user():
    print("Hello! I'm your personal assistant chatbot. How can I help you today?")

# Function to handle user input
def chatbot():
    greet_user()
    
    # A simple loop to keep the conversation going
    while True:
        user_input = input("\nYou: ").lower()  # Get user input and convert to lowercase
        
        # Simple responses based on predefined questions
        if "hi" in user_input or "hello" in user_input:
            print("Chatbot: Hi there! How can I assist you?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but thanks for asking! How about you?")
        
        elif "time" in user_input:
            current_time = time.strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}.")
        
        elif "remind me" in user_input:
            reminder = input("Chatbot: Sure! What would you like me to remind you about? ")
            reminder_time = input("Chatbot: When should I remind you? (format: HH:MM) ")
            print(f"Chatbot: Got it! I'll remind you to '{reminder}' at {reminder_time}. (Note: This is a mock reminder system)")
        
        elif "what is your name" in user_input:
            print("Chatbot: My name is Chatbot. What's yours?")
        
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Fallback response if no match is found
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Could you please rephrase?")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
