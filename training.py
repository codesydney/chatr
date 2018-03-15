from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Calo")

conversation = [
    "What is Code.Sydney?",
    "A group of volunteer pythonistas!",
    "Who are in the team?",
    "Engramar, Steve, Mathu, Gagan and Bin",
    "Great",
    "Thank you.",
    "You're welcome."
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)