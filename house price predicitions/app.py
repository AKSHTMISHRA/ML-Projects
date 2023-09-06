from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///HOUSE_PRICES.db"
db=SQLAlchemy(app)



@app.route("/")
@app.route("/home")
@app.route("/homepage")
@app.route("/index")
def homepage():
    return render_template('index.html',login=False)

@app.route("/predictor")
def Predictor():
    return render_template('predictor.html')

@app.route("/view_directory")
def Search():
    return render_template('Search_dir.html')

@app.route("/Contact_us")
def Contact_us():
    return render_template('contact_us.html')

@app.route("/login")
@app.route("/Login")
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True,port=8000)