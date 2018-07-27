import os
from datetime import datetime
from flask import Flask, redirect, render_template, request

app = Flask(__name__)


def write_to_file(filename, data):
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)


def add_messages(username, message):
    """Add messages to the `messages` text file"""
    write_to_file("data/users.txt", "({0}) {1} - {2}\n".format(
            datetime.now().strftime("%H:%M:%S"),
            username.title(),
            message))


def get_all_messages():
    """Get all of the messages and separate them by a `br`"""
    messages = []
    with open("data/users.txt", "r") as chat_messages:
        messages = chat_messages.readlines()
    return messages


def get_users():
    """Get all of the messages and separate them by a `br`"""
    users = []
    with open("data/users.txt", "r") as user_messages:
        messages = user_messages.readlines()
    return 
    

@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    
    # Handle POST request
    if request.method == "POST":
        write_to_file("data/users.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")


@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    """Display chat messages"""
    
    if request.method == "POST":
        add_messages(username, request.form["message"] + "\n")
    
    messages = get_all_messages()
    return render_template("r.html",
                            username=username, chat_messages=messages)


@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect(username)

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)