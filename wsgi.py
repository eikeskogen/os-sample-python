from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "eikeskogen 3"

if __name__ == "__main__":
    application.run()
