import spacy

nlp = spacy.load("en_core_web_sm")  # Load the English language model

# Use the nlp object to process some text


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
bot = ChatBot(
    "My Chatbot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="sqlite:///database.db"
)

# Train the chatbot using the English corpus
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

# Start the chatbot and allow the user to interact with it
print("Chatbot is ready to talk! Type 'quit' to exit.")
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = bot.get_response(user_input)
        print("Chatbot: ", response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
