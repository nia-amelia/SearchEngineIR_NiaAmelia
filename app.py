from flask import Flask, render_template, request
from src.search_function import search_books, df

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    results = None
    query = ""

    total_books = len(df)

    if request.method == "POST":

        query = request.form["query"]

        results = search_books(query)

    return render_template(
        "index.html",
        results=results,
        query=query,
        total_books=total_books
    )

import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )