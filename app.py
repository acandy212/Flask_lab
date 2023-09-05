from flask import Flask, render_template, request          # import flask framework
app = Flask(__name__)             # create an app instance

@app.route("/")                   # use the home url
def hello():                      # method called hello
    return render_template("index.html")        # returns "hello world"

@app.route("/<name>")              # route with URL variable /<name>
def hello_name(name):              # call method hello_name
    return "Hello "+ name          # which returns "hello + name  

@app.route("/about")
def about():
    name = request.arg.get('name')
    return render_template("about.html", aboutName=name)  
    name = request.args.get('name') if request.args.get('name') else "Hello World!" 

if __name__ == "__main__":        # when running python app.py
    app.run()                     # run the flask app

#change app.run() to the following
app.run(debug=True)    


