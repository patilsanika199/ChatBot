from flask import Flask, render_template, jsonify,request
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://patilsanika199:sanu4462@chatbot1.nqiqjnt.mongodb.net/chatbot"
mongo = PyMongo(app)


@app.route("/")
def history():
    chats = mongo.db.chats.find({}, {"question": 1}).sort("_id", -1).limit(10)
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("history.html", myChats=myChats)

@app.route("/api", methods=["POST"])
def qa():
    if request.method == "POST":
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question": question})
        if chat:
            data = {"result": chat["answer"]}   
        else:
            mongo.db.chats.insert_one({"question":   question, "answer": f"Answer from openai for {question}"})
            data = {"result": f"Answer of {question}"}
        return jsonify(data)

if __name__ == "__main__":

    app.run(debug=True,port=5002)
