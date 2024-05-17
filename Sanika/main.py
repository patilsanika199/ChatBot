from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import certifi
import ssl
import json
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__, template_folder='template')

app.config["MONGO_URI"] = "mongodb+srv://patilsanika199:sanu4462@chatbot1.nqiqjnt.mongodb.net/chatbot"
mongo = PyMongo(app)

# Load the ML model and data
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('tfidf_matrix.pkl', 'rb') as f:
    tfidf_matrix = pickle.load(f)

chats = pd.read_pickle('chats.pkl')

@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html", myChats=myChats)


def get_answer(question):
    query_vector = vectorizer.transform([question])
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    best_match_idx = similarities.argmax()
    if similarities[best_match_idx] > 0.1:  # You can set a threshold for similarity
        return chats.iloc[best_match_idx]['answer']
    else:
        return None
    


@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question": question})
        print(chat)
        if chat:
            data = {"result": f"{chat['answer']}"}
            return jsonify(data)
        else:
            answer = get_answer(question)
            if answer:
                data = {"result": answer}
            else:
                data = {"result": f"Answer from OpenAI for {question}"}
                mongo.db.chats.insert_one({"question": question, "answer": data["result"]})
            return jsonify(data)
    data = {"result": "Hey, I am a chatbot"}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
