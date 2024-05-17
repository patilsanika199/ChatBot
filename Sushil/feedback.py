from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://patilsanika199:sanu4462@chatbot1.nqiqjnt.mongodb.net/chatbot"
mongo = PyMongo(app)

@app.route('/')
def query_form():
    return render_template('Feedback.html')

@app.route('/submit_query', methods=['POST'])
def submit_query():
    name = request.form['name']
    email = request.form['email']
    query = request.form['query']
    Feedback = {'name': name, 'email': email, 'query': query}
    mongo.db.Feedback.insert_one(Feedback)
    return jsonify({'message': 'Your query has been submitted successfully!'})

if __name__ == '__main__':
    app.run(debug=True , port=5001)
