import string
import random
from flask import Flask, request, redirect

app = Flask(__name__)

# Dictionary to store the mappings of short codes to long URLs
url_mappings = {}


def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))
    return short_code


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        long_url = request.form["long_url"]
        short_code = generate_short_code()
        url_mappings[short_code] = long_url
        return f"Short URL: {request.url_root}{short_code}"
    return "Welcome to the URL Shortener!"


@app.route("/<short_code>")
def redirect_to_long_url(short_code):
    if short_code in url_mappings:
        long_url = url_mappings[short_code]
        return redirect(long_url, code=302)
    return "URL not found."


if __name__ == "__main__":
    app.run(debug=True)
