#!/usr/bin/python

import time
from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
    return "Hello World 1"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8083)
