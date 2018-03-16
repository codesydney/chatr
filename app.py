from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from werkzeug import secure_filename

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

#english_bot.set_trainer(ChatterBotCorpusTrainer)
#english_bot.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))

@app.route('/train', methods = ['GET', 'POST'])
def upload():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      conversation = open(f.filename,'r').readlines()
      english_bot.set_trainer(ListTrainer)
      english_bot.train(conversation)
      return 'Chatbot successfully trained with new data. Please test.'
   return render_template('train.html')
if __name__ == "__main__":
    app.run()