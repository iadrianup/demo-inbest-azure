# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.
from flask import Flask, render_template, send_from_directory, request, send_file



# Initialize the Flask app
app = Flask(__name__)

# Load configuration
# app.config.from_object('config.BaseConfig')

@app.route('/')
def index():
    '''Returns a static HTML page'''

    return render_template('index.html')



# app.run()