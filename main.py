from flask import Flask
from flask import Flask, render_template
import pandas as pd

df = pd.read_csv("Rooms.csv")



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/data")
def datas():
    return df.to_html()

@app.route("/describe")
def describe():
    Info = df.describe()
    return Info.to_html()

'''
@app.route('/')
def home():
    ase = open("index.html")
    return ase
'''


@app.route("/Waifu")
def waifu():
    return render_template('Shigure.html')

app.run(port=6969, debug=True)
