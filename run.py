import os
import json
from datetime import datetime
from flask import Flask, redirect, render_template, request, flash



app = Flask(__name__)
app.secret_key = 'some_secret'


def write_to_file(filename, data):
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)
        
def add_players(username, message):
    """Add messages to the `messages` text file"""
    write_to_file("static/data/users.txt", "({0}) {1} - {2}\n".format(
            datetime.now().strftime("%H:%M:%S"),
            username.title(),
            message))

            
            
def get_all_players():
    """Get all of the players names from the 'players. text file"""
    users = []
    with open("static/data/messages.txt", "r") as user_messages:
        users = user_messages.readlines()
    return users  



@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    
    # Handle POST request
    if request.method == "POST":
        write_to_file("static/data/users.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")
    
    

@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    """Display chat messages"""
    
    if request.method == "POST":
        add_players(username, request.form["message"] + "\n")
    
    messages = get_all_players()
    return render_template("riddlegame.html",
                            username=username, chat_messages=messages)
                            



@app.route('/about')
def about():
    data = []
    with open("static/data/riddledata.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)




@app.route('/about/<member_name>')
def about_member(member_name):
    member = {}
   
    with open("static/data/riddledata.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
   
    return render_template("riddlegame.html", member=member)





@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message".format(
            request.form["name"]
        ))
    return render_template("contact.html", page_title="Contact")





@app.route('/careers')
def careers():
    return render_template("careers.html", page_title="Careers")





if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)