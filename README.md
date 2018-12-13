# BMI calculator

I decided to do a simple BMI calculator instead of a riddle game for the Python Milestone Project, as I found Python difficult when it comes to make a logic based game, due to work conflicts and personal circumstances that have occured during the year. 
I personally feel that this is a straightforward way to make a Python project with Flask, as I can understand the code better. Credit to Udemy for the tutorial. 
 
## UX
 

- As a user type, I want to know my BMI
- As a user, I want to use a app that can calculate my BMI
- As a user, I want to have a place to input my information.
- As a user, I want to have a result from inputting my information.
- As a user, I want the design to be clean and straightforward.


## Features

There are two input spaces for the user to type in their height (in cms) and weight (in kgs). 
When they hit submit, it should calculate their body mass index.

## Technologies Used

- [HTML](https://www.w3schools.com/html/)
- [CSS](https://www.w3schools.com/css/default.asp)
- [Python](https://www.python.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Jinja2](http://jinja.pocoo.org/docs/2.10/)

## Testing

Index.html
- Click on link
- Go to the calculator
- Input weight and height
- Click Submit

If the site is running, a BMI results should appear.

## Deployment

How to deploy to Heroku:

First, create a new Heroku account and create new app. Then type the following into terminal:

- $heroku 
- $heroku login
- $heroku apps
- $git remote -v
- $git remote add heroku https://github.com/ainedoyle/3rd-milestone
- $git push -u heroku master
- $sudo pip3 freeze --local > requirements.txt
- $echo web: python run.py > Procfile
Deployed at: https://third-milestone-project.herokuapp.com/

## Credits


### Content

https://getbootstrap.com/docs/4.0/layout/grid/

https://www.udemy.com/python-flask-for-beginners/learn/v4/overview

https://pixabay.com/en/apple-healthy-fruit-calories-red-3851446/


### Media
- The photos used in this site were obtained from Pixabay

### Acknowledgements

- I received inspiration for this project from X

Code Institute 

Udemy

Pixabay

