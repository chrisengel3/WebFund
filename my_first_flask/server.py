from flask import Flask, render_template

app = Flask(__name__) #this creates a new instance of the Flask class

@app.route("/") # The Index Route
def index():
    # return "Hello World!"
    return render_template("index.html", phrase="hello", times=5)

# ALL ROUTES NEED TO START WITH A / (JUST LIKE THE /USER ETC IN A URL)
@app.route("/hello/something")
def hello():
    return "awwwwwwwe yeah hey!"

@app.route("/dojo")
def dojo():
    return "DOJO!"

# # PATH VARIABLE
@app.route("/say/<name>")
def name_caller(name):
    return f"awwwwwwwe yeah hey {name}!"


@app.route("/spam/<int:repeat>/<word>") #???????
def spam(repeat, word):
    if word.isdigit() == False: 
        return f"here it comes... {word * repeat}!"
    else: return "scsdfsdfsdg"

# @app.route("/users/<username>/<int:id>")
# def hello(username, id):
#     print(type(username))
#     print(type(id))
#     return f"awwwwwwwe yeah hey {username}!"

if __name__ == "__main__":
    app.run(debug = True)
