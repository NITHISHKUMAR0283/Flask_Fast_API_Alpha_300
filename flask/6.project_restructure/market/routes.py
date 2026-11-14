from market import app
from flask import  render_template
from market import model
from market.model import Item

@app.route('/')
@app.route('/home')
def home():
    return render_template('/home.html')
@app.route('/market')
def market():
    item = Item.query.all()
    print(item)
    return render_template('/market.html',items=item)
