from flask import Flask, request

app = Flask("hello_world_app")


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/apple")
def apple():
    return "Apple!"


@app.route("/slava")
def slava():
    return f"The name is: {request.args.get('name')}"


if __name__ == '__main__':
    # app.run(host=0.0.0.0, port=5555)
    app.run(debug=True, port=5001)
