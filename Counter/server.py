
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe."

# what is the default request method when declaring a route?
# GET Request
@app.route("/")
def index():
    session['amount'] += 1
    return render_template("index.html")

@app.route("/destroy")
def destroy():
    session.clear()
    session['amount'] = 0
    # session.pop('secret_key')
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug = True)
