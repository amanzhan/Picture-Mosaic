from PictureMosaic.picture_processor import generate_mosaic
import os
from pathlib import Path
import flask
from flask import Flask, request, redirect, url_for
from config import SOURCE_DIR, UPLOAD_FOLDER
from __init__ import app

counter = 0

def remove_old():
    paths = sorted(Path(UPLOAD_FOLDER).iterdir(), key=os.path.getmtime)
    if len(paths) > 10:
        os.remove(paths[0])

@app.route('/', methods=['GET', 'POST'])
def index():
    global counter
    remove_old()
    if request.method == "POST":
        file = request.files['picture']
        filename = str(counter) + ".jpg"
        filename = os.path.join("inputs", filename)
        counter += 1
        file.save(filename)
        final_pic = generate_mosaic(filename)
        
        return redirect(url_for('results', filename=final_pic))
    context = {}
    return flask.render_template("index.html", **context)