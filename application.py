from flask import Flask
application = Flask(__name__)

@application.route("/")
def index():
    return "Your Flask App Works!"

@application.route("/hello")
def hello():
    name = "SilconTechLabs"
    return "Hello !" + name + "!\n"


if __name__ == "__main__":
    application.run(port=8000, debug=True)