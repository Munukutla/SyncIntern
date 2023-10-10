"""Chatbot project for Sync intern's Python Internship"""
#importing modules
import nltk
import random
from nltk.chat.util import Chat, reflections
#Defing questions and answers for the chat which is pre-defined
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am just a chatbot.', 'I am fine, thank you.']),
    (r'what is your name', ["I'm a chatbot, I don't have a name."]),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
    (r'happy new year', ['happy new year', 'Same to you']),
    (r'today is my birthday', ['Happy birthday to you', 'Many many happy returns of the day']),
    (r'good morning', ['Good morning ,have a nice day']),
    (r'thanks for your company', ['thank you too for your company.', 'Its my pleasure.']),
]

# Create a chatbot with Chat function
chatbot = Chat(patterns, reflections)
#starting conversation with chatbot
print("Chatbot: Hi! How can I assist you today? (type 'exit' to end)")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    else:
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
