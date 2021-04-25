from flask import Flask, render_template
import os
import tensorflow_chessbot as chess
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html');

@app.route('/test')
def chessImage():
    return chess.main("static/img/chess2.png");