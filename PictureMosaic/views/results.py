import os
import flask
from flask import Flask, request
from config import SOURCE_DIR
from __init__ import app


@app.route('/results/<filename>/', methods=['GET', 'POST'])
def results(filename):
    print("inside results")
    
    context = {"filename": filename}
    return flask.render_template("results.html", **context)