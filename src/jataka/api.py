""" a simple api, randomly returns jataka stories."""

import json
import random

import flask
from flask import Flask

from preprocess import save_json

app = Flask(__name__)


def open_json(fname: str) -> dict:
    """open json story book and return as dict."""
    with open(f"./data/json/{fname}.json", "r") as fh:
        return json.load(fh)


def random_sentence(story: dict) -> str:
    """pick a random sentence from the story."""
    string = random.choice(list(story.values()))
    if len(string) < 50:
        return random_sentence(story)
    return string.replace('"', "")


@app.route("/jataka", methods=["GET"])
def jataka():
    save_json("jataka")
    story = open_json("jataka")
    quote = random_sentence(story)
    return flask.jsonify(quote)


@app.route("/", methods=["GET"])
def index() -> None:
    return flask.jsonify("Random jataka tale sentences.")


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
