from flask import Flask, jsonify, render_template, request

import os, optparse
import yaml
with open("links.yaml", 'r',encoding='utf-8') as stream:
    try:
        info = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
environment = os.getenv("ENVIRONMENT", "development")

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("template.html", info=info)


if __name__ == "__main__":
    debug = False
    if environment == "development" or environment == "local":
        debug = True
    app.run(host="0.0.0.0", debug=debug)

