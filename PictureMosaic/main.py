from PictureMosaic.picture_processor import compile_source_file_data
import os
import flask
from flask import Flask, request
from config import SOURCE_DIR
from __init__ import app


if __name__ == "__main__":
    # TODO: process picture
    source_files = os.listdir(SOURCE_DIR)
    compile_source_file_data(source_files)
    app.run()