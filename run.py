import os
from datetime import datetime
from flask import Flask, render_template, request, redirect

# Set to current function
app = Flask(__name__)


# To access page and input information
@app.route('/', methods=["GET", "POST"])
#Function
def index():
    
    bmi = ''
    
    # To grab data
    if request.method == 'POST' and 'weight' in request.form:
        
        # Float number
        weight = float(request.form.get('weight'))
        
        #Float number
        height = float(request.form.get('height'))
        
        #Passing variables to function
        bmi = calc_bmi(weight, height)
        
    # To run page
    return render_template("index.html", bmi=bmi)
    


def calc_bmi(weight, height):
    #Weight is divided by the height in meters squared
    #The answer needs to be rounded
    return round((weight / ((height / 100) ** 2)), 2)



# To execute the code
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)


