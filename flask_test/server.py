
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe."

# what is the default request method when declaring a route?
# GET Request
@app.route("/")
def index():
    return render_template("index.html")


# NEVER RENDER ON A POST REQUEST ALWAYS REDIRECT TO A NEW ROUTE
@app.route("/create", methods = ["POST"])
def create_dog():
    print(request.form)
    #request.form is a dictionary
    #session is a dictionary
    session['name'] = request.form['name']
    session['age'] = request.form['age']
    session['hair_color'] = request.form['hair_color']
    (request.form['age'])
    (request.form['hair_color'])

    return redirect("/display") # REDIRECT MAKES A NEW GET REQUEST

@app.route("/display")
def display():
    print(session['name'])
    print("SUCCESSFUL REDIRECT")
    return render_template('display.html')


if __name__ == "__main__":
    app.run(debug = True)
