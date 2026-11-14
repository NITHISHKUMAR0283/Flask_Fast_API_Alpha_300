from flask import Flask
app = Flask(__name__)

@app.route("/")
def home ():
    return '<h1>This is home page</h1>'

@app.route("/about/<username>")
def about (username):
    return f'<h1> this is about page of {username}'

if __name__=='__main__':
    app.run(debug=True)