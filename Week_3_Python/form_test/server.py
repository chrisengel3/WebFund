from flask import Flask, render_template, request
app = Flask(__name__)
# our index route will handle rendering our form


app.route('/')
def index():
    return render_template("index.html")


@app.route("/create", methods = ["POST"])
def create_dog():
    print(request.form)

    return render_template("display.html")

if __name__ == "__main__":
    app.run(debug=True)

