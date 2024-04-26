from flask import Flask , render_template ,jsonify, request
from flask_pymongo import PyMongo
import certifi
import ssl


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Chatbot"
mongo = PyMongo(app)

app = Flask(__name__, template_folder='template')

@app.route("/")
def home():
        chats = mongo.db.chats.find({})
        myChats=[chat for chat in chats]
        print(myChats)
        return render_template("index.html", myChats=myChats)

@app.route("/api", methods=["GET","POST"])
def qa():
        if request.method == "POST":
                print(request.json)
                question = request.json.get("question")
                chat = mongo.db.chats.find_one({"question":question})
                print(chat)
                if chat :
                        data={"result": f"{chat['answer']}"}
                        return jsonify(data)
                else:
                        data = {"result":f"Answer of {question}" } 
                        mongo.db.chats.insert_one({"question":question, "answer": f"Answer from openai for {question}"})
                        return jsonify(data)
        data = {"result":"Hey i am chatbot "}
        return jsonify(data)        
       
    
app.run(debug=True)
    
    