from flask_pymongo import PyMongo
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/local"
mongo = PyMongo(app)

@app.route('/write', methods=["POST"])
def write():
    name = request.form.get('name')
    content = request.form.get('content')

    mongo.db['market'].insert_one({
        "name": name,
        "content": content
    })

    return redirect('/')

@app.route('/')
def index():

    return render_template('list.html')

if __name__ == '__main__':
    app.run()
