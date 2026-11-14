from flask import Flask,render_template

app = Flask(__name__)

data = [
    12,3,4,5,3,2,1,3,4,5,3,2,3,232,2323,232,44,2
]

@app.route('/')
@app.route('/home')
def home():

    return render_template('index.html',name = "nithish" , id = "RA2411026011347",data = data)
if __name__=='__main__':
    app.run(debug=True)