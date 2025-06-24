#!/usr/bin/python3
"""A script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable
(replace underscore _ symbols with a space )
/python/(<text>): display “Python ”, followed by the value of the text
variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
/number_odd_or_even/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n is even|odd” inside the tag BODY
You must use the option strict_slashes=False in your route definition"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hhbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def croute(text="is cool"):
    new_text = " ".join(text.split("_"))
    return f"C {new_text}"


@app.route('/python', strict_slashes=False)
def py_route():
    return "Python is cool"


@app.route('/python/<text>', strict_slashes=False)
def pyroute(text="is cool"):
    new_text = " ".join(text.split("_"))
    return f"Python {new_text}"


@app.route('/number/<int:n>', strict_slashes=False)
def numroute(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template_route(n):
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even_route(n):
    odd_or_even = "odd" if n % 2 == 1 else "even"
    return render_template('6-number_odd_or_even.html',
                           odd_or_even=odd_or_even, n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
