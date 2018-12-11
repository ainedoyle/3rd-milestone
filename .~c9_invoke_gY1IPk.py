import os
import json
from datetime import datetime
from flask import Flask, redirect, render_template, request, flash, url_for, redirect, jsonify, session


app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "not a secret")



def write_to_file(filename, data):
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)
        

MAX_ATTEMPTS = 3
       f = open("stat.txt", "r")
    RIDDLES = json.load(riddle_file)

high_score = {
    "name": "nobody",
    "score": 0
}


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/new_game", methods=["POST"])
def new_game():
    session["player"] = request.form["player"]
    if request.method == "POST":
        write_to_file("static/data/users.txt", request.form["player"] + "\n")

    session["score"] = 0
    session["riddle_num"] = 0
    session["riddle_attempts"] = MAX_ATTEMPTS
    return redirect(url_for("riddle"))
    


@app.route("/riddle", methods=["GET", "POST"])
def riddle():
    if "player" not in session:
        return redirect(url_for("index"))

    if request.method == "POST" and session["riddle_num"] < len(RIDDLES):
        
        previous_riddle = RIDDLES[session["riddle_num"]]
        
        if request.form["answer"].lower() == previous_riddle["answer"]:
            
            session["riddle_num"] += 1
            session["score"] += 1
            
            if session["riddle_num"] < len(RIDDLES):
                flash("Correct answer, %s! Your score is %s." % (
                      session["player"], session["score"]))
            else:
                flash("Correct answer, %s!" % session["player"])
                
                
        elif not session["riddle_attempts"]:
            session["riddle_num"] += 1
            session["riddle_attempts"] = MAX_ATTEMPTS
            if session["riddle_num"] < len(RIDDLES):
                flash("Wrong answer, %s. Better luck with this riddle:" % (
                      session["player"]))
        else:
            session["riddle_attempts"] -= 1
            flash("Wrong answer, %s. You have %s attempts left." % (
                  session["player"], session["riddle_attempts"]))
                  
                  
                  

    if session["riddle_num"] >= len(RIDDLES):
        if session["score"] >= high_score["score"]:
            high_score["score"] = session["score"]
            high_score["name"] = session["player"]
        return render_template("endofgame.html", player=session["player"],
                               score=session["score"],
                               highscore=high_score["score"],
                               highscorer=high_score["name"])
                               
                               

    new_riddle = RIDDLES[session["riddle_num"]]
    return render_template("riddlegame.html", 
                             player=session["player"],
                             question=new_riddle["question"], 
                             riddle_num=session["riddle_num"])


if __name__ == "__main__":
    app.run(os.getenv("IP", "0.0.0.0"), 
            port=int(os.getenv("PORT", "8080")),
            debug=True)