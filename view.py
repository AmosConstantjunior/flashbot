
from flask import Flask, render_template, request
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['moteur_recherche']
collection = db['flashbot']



app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',  methods = ['POST'] )
def result():
    
    donnee = request.form.get('search_1')
    def verifier():
        if donnee in db.flashbot.find():
            return db.flashbot.find()
    
    results = verifier().sort([("pubDate", -1)])

    return render_template('result.html', resultat=donnee)

if __name__ == "__main__":
    app.run()
