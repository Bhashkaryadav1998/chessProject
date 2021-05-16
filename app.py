from flask import Flask, render_template, request, json, redirect
import os

from werkzeug.utils import secure_filename

import tensorflow_chessbot as chess
app = Flask(__name__)
UPLOAD_FOLDER = 'static/img/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
host = 'localhost'
app.logger.info('Server started')

@app.route('/')
def hello_world():
    app.logger.info('index.html loaded')
    return render_template('index.html')


@app.route('/upload',methods=['POST'])
def chessImage():
    app.logger.info('Received request on upload page')
    if 'file' not in request.files:
        app.logger.error('No File part received')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        app.logger.error('No image received for analysis')
        return redirect(request.url)
    app.logger.info('Image received for fen conversion')
    flip=request.form['flip']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    app.logger.info('Analysis started on Image')
    fen=chess.main('static/img/uploads/'+filename,flip)
    app.logger.info('Analysis finished and fen is sent')
    return json.dumps(fen)