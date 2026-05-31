from flask import Flask, render_template, request
from src.search_function import search_books, df

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    results = None
    query = ""

    page = 1

    total_books = len(df)
    

    if request.method == "POST":

        query = request.form["query"]
        results = search_books(query)
        page = 1
    else:
        query = request.args.get("query", "")
        if query:
            results = search_books(query)
        else:
            results = None

    if results is not None:

        per_page = 5

        total_results = len(results)

        page = int(request.args.get("page", 1))

        start = (page - 1) * per_page

        end = start + per_page

        paginated_results = results.iloc[start:end]

        has_next = end < total_results

        has_prev = page > 1

    else:

        paginated_results = None

        has_next = False

        has_prev = False

    return render_template(
    "index.html",
    results=paginated_results,
    query=query,
    total_books=total_books,
    has_next=has_next,
    has_prev=has_prev,
    page=page
)

import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )