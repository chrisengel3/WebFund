from flask import Flask, render_template

app = Flask(__name__) #this creates a new instance of the Flask class

@app.route("/") # The Index Route
def index():
    return "Hello World!"
    # return render_template("index.html", phrase="hello", times=5)


if __name__ == "__main__":
    app.run(debug = True)
