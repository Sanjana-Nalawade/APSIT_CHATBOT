from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
chatbot = ChatBot('APSIT')
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train("chatterbot.corpus.english")
conv1=open('college_detail1.yml','r').readlines()
#conv2=open('faculty_detail1.yml','r').readlines()
#conv3=open('navigation_detail1.yml','r').readlines()
#conv4=open('chatbot_detail1.yml','r').readlines()
trainer=ListTrainer(chatbot)
trainer.train(conv1)
#trainer.train(conv2)
#trainer.train(conv3)
#trainer.train(conv4)
