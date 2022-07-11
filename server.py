from flask import Flask


the_app = Flask(__name__)


@the_app.route('/')
def intro_page():
    return 'Hello World!'


if __name__ == "__main__":
    the_app.run(debug=True)
