from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Potentially promising. Just for dun Hello World Updated!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
