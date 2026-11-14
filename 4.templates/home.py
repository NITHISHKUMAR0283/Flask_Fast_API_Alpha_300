from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('/home.html')
@app.route('/market')
def market():
    return render_template('/market.html',items = [    {"id": 5, "name": "Nithish"},
    {"id": 6, "name": "Laptop"},
    {"id": 7, "name": "Wireless Mouse"},
    {"id": 8, "name": "Mechanical Keyboard"},
    {"id": 9, "name": "Monitor"},
    {"id": 10, "name": "Headphones"}])

if __name__=="__main__":
    app.run(debug="True")