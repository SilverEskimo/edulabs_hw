from flask import Flask, request, jsonify
from db_connector import DBConnector
app = Flask("Bank Application")
db = DBConnector()


@app.route("/api/v1/accounts")
def get_accounts():
    filters = request.args if request.args else None
    res = db.get_accounts(filters)
    return jsonify(res) if res else app.response_class(status=404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)