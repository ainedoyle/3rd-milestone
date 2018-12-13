import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, json

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    bmi = ''
    if request.method == 'POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = calc_bmi(weight, height)
    return render_template("index.html", bmi=bmi)
    



def calc_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)), 2)


app.run(host=os.getenv('IP'), 
                port=int(os.getenv('PORT')), 
                debug=True)


