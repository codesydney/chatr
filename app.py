from flask import Flask, render_template, request, redirect, url_for
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from werkzeug import secure_filename

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.english.greetings")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))

@app.route("/login", methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['token'] == '123456':
          return redirect(url_for('upload'))
        error = 'Incorrect token. Please try again.'
    return render_template("login.html", error=error)

@app.route('/training', methods = ['GET', 'POST'])
def upload():
    msg = None
    if request.method == 'POST':
      if request.files['file']:
        f = request.files['file']
        f.save(secure_filename(f.filename))
        conversation = open(f.filename,'r').readlines()
        english_bot.set_trainer(ListTrainer)
        english_bot.train(conversation)
        msg = 'Chatbot successfully trained with new data. Please test by going back to the Demo page.'
      else:
        msg = 'Please upload a file containing your training data.'        
    return render_template('training.html', msg=msg)

if __name__ == "__main__":
    app.run(debug=True)