
from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe."

# what is the default request method when declaring a route?
# GET Request
@app.route("/")
def index():
    if "newGold" not in session:
        session['newGold'] = 0
    if "goldCount" not in session:
        session['goldCount'] = 0
    return render_template("index.html")


@app.route("/getrich", methods = ["POST"])
def get_rich():
    if request.form['source'] == 'farm':
        session['currentGold'] = session['goldCount']
        session['newGold'] = random.randint(10,20)
        session['goldCount'] += session['newGold']
    if request.form['source'] == 'cave':
        session['currentGold'] = session['goldCount']
        session['newGold'] = random.randint(5,10)
        session['goldCount'] += session['newGold']
    if request.form['source'] == 'house':
        session['currentGold'] = session['goldCount']
        session['newGold'] = random.randint(2,5)
        session['goldCount'] += session['newGold']
    if request.form['source'] == 'casino':
        session['currentGold'] = session['goldCount']
        session['newGold'] = random.randint(-50,50)
        session['goldCount'] += session['newGold']
    return redirect("/")

# # NEVER RENDER ON A POST REQUEST ALWAYS REDIRECT TO A NEW ROUTE
# @app.route("/process", methods = ["POST"])
# def dojo_survey():
#     print(request.form)
#     #request.form is a dictionary
#     #session is a dictionary
#     session['name'] = request.form['name']
#     session['Dojo_Location'] = request.form['Dojo_Location']
#     session['Favorite_Language'] = request.form['Favorite_Language']
#     session['comments_optional'] = request.form['comments_optional']

#     return redirect("/result") # REDIRECT MAKES A NEW GET REQUEST

# @app.route("/result")
# def display():
#     # print(session['name'])
#     # print("SUCCESSFUL REDIRECT")
#     return render_template('results.html')


if __name__ == "__main__":
    app.run(debug = True)
