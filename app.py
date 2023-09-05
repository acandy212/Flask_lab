from flask import Flask           # import flask framework
app = Flask(__name__)             # create an app instance

@app.route("/")                   # use the home url
def hello():                      # method called hello
    return "Hello World!"         # returns "hello world"

@app.route("/<name>")              # route with URL variable /<name>
def hello_name(name):              # call method hello_name
    return "Hello "+ name          # which returns "hello + name  

if __name__ == "__main__":        # when running python app.py
    app.run()                     # run the flask app

#change app.run() to the following
app.run(debug=True)    


