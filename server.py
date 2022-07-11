from flask import Flask, render_template


the_app = Flask(__name__)


@the_app.route('/')
def intro_page():
    return render_template('index.html')


if __name__ == "__main__":
    the_app.run(debug=True)
