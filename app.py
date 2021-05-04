from flask import Flask, render_template, request, json
import os

from werkzeug.utils import secure_filename

import tensorflow_chessbot as chess
app = Flask(__name__)
UPLOAD_FOLDER = 'static/img/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/upload',methods=['POST'])
def chessImage():
    file = request.files['file']
    flip=request.form['flip']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    fen=chess.main('static/img/uploads/'+filename,flip)
    return json.dumps(fen)