"""
Insta485  view.

URLs include:
/
"""
from config import UPLOAD_FOLDER
import flask
from flask import Flask, request, send_from_directory
from __init__ import app


@app.route('/uploads/<filename>', methods=['GET'])
def upload(filename):
    
    """Display /uploads/<image> route."""
    return send_from_directory(
        UPLOAD_FOLDER,
        filename, mimetype='image/jpg'
    )
