#!/usr/bin/env python

import requests
from flask import Flask, request, jsonify


CON_URL = "http://con:6064"


HOST: str = "0.0.0.0"
PORT: int = int(os.getenv("MODULE_PORT"))


app = Flask(__name__)


@app.get("/")
def index():
    print('Connected to', HOST, PORT)


def main():
    print(f"Starting server at {HOST}:{PORT}")
    app.run(port=PORT, host=HOST)
