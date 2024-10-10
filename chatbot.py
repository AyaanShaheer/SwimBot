import nltk
import random

# Downloading necessary NLTK data (if not already available)
nltk.download('punkt')
nltk.download('punkt_tab')
# Initializing some sample data for Castle Swimmer chapters 83-89
knowledge_base = {
    "what is castle swimmer about": [
        "Castle Swimmer is a webcomic about a young merman named Kappa who is the Beacon, a figure prophesied to guide various underwater kingdoms to their destinies."
    ],
    "who are the main characters": [
        "The main characters are Kappa, a merman and the Beacon, and Siren, the prince of the Shark Kingdom."
    ],
    "tell me about the prophecy": [
        "The prophecy says that the Beacon, Kappa, must help the Shark Kingdom by guiding them to fulfill their destiny, but this comes with great challenges."
    ],
    "what happens in chapter 83": [
        "In Chapter 83, tensions rise as Kappa faces the consequences of the prophecy, and the characters struggle with difficult decisions."
    ],
    "what happens in chapter 89": [
        "In Chapter 89, there is a significant turning point where Kappa's role in the prophecy becomes clearer, and new revelations come to light."
    ]
}

# Defining fallback responses for when the bot doesn't understand the input
fallback_responses = [
    "I'm not sure I understand. Could you rephrase that?",
    "Sorry, I don't have information on that yet. Try asking something else.",
    "I couldn't find an answer for that. Can you ask about the plot or characters?"
]

def get_response(user_input):
    # Tokenize and normalize the user input
    user_input = user_input.lower()
    tokens = nltk.word_tokenize(user_input)

    # Look for keywords in the knowledge base
    for key in knowledge_base.keys():
        if any(word in key for word in tokens):
            # Select a random response from the matching answers
            return random.choice(knowledge_base[key])
    
    # If no keywords match, return a fallback response
    return random.choice(fallback_responses)

# Chatbot interaction example
def chatbot():
    print("Castle Swimmer Bot: Hello! You can ask me about Castle Swimmer. Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Castle Swimmer Bot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Castle Swimmer Bot: {response}")


chatbot()
