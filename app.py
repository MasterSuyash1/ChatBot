import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['hi', ['Hello!', 'Hi there!', 'Greetings!']],
    ['how are you', ['I am doing well, thank you.', 'I am great, thanks for asking.']],
    ['what is your name', ['I am a chatbot.', 'You can call me Chatbot.']],
    ['bye', ['Goodbye!', 'See you later!', 'Take care!']],
    ['what is your favourite color', ['I like orange.', 'I like all colors.']],
    ['what is your favourite food', ['I like chole bhature.', 'I like chole kulche.',"I like all food."]],
    ["what is your lucky number", ["1", "I like all numbers."]],
]
def chatbot():
    chatbot = Chat(pairs, reflections)
    print("Hello! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit' or user_input.lower() == 'exit':
            break
        response = chatbot.respond(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    chatbot()

