"""split the text into phrases."""

import json
import os


def split(fh) -> dict:
    """split text into lines, return cleaned up dict."""
    lines = {}
    for i, v in enumerate(cleanup(fh.readlines())):
        lines[i] = v
    return lines


def cleanup(lines: list):
    """remove empty values and only return content."""
    lower = lambda inp: inp.lower()
    rm_newline = lambda inp: "\n"
    begin_book = "distributed proofreading team"
    lines = [l.rstrip() for l in lines]
    lines = list(map(lower, lines))
    lines = list(filter(rm_newline, lines))
    lines = list(filter(None, lines))
    start_idx = lines.index(begin_book)
    end_idx = 307  # quick hack
    return lines[start_idx + 1 : -end_idx]


def open_book(fname: str) -> dict:
    "open book and return as list of sentences."
    text_file = f"./data/text/{fname}.txt"
    with open(text_file) as fh:
        return split(fh)


def save_json(fname: str) -> None:
    """save process text book as json."""
    json_file = f"./data/json/{fname}.json"
    lines = open_book(fname)
    if not os.path.isfile(json_file):
        with open(json_file, "w") as fh:
            json.dump(lines, fh)


if __name__ == "__main__":
    save_json("jataka")
