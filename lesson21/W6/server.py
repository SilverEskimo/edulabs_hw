import uuid
from src.my_spacy import MySpacy
from flask import Flask, request, jsonify
from concurrent.futures import ThreadPoolExecutor


app = Flask("NLP_WEB_Server")
my_spacy = MySpacy()
executor = ThreadPoolExecutor()
@app.route("/api/v1/sentences", methods=['POST'])
def sentences():
    return jsonify(my_spacy.sentences(request.form))


@app.route("/api/v1/pos", methods=['POST'])
def pos():
    query_params = request.args if request.args else None
    return jsonify(my_spacy.pos(request.form, query_params))


@app.route("/api/v1/named_ents", methods=['POST'])
def named_entities():
    task_id = uuid.uuid4()
    res = {
        "task_id": task_id
    }
    executor.submit(my_spacy.named_entities, request.form, task_id)
    return jsonify(res)


@app.route("/api/v1/tasks/<uuid:task_id>/status", methods=['GET'])
def get_status(task_id):
    return jsonify(
        {
            "status": my_spacy.get_state(task_id)
        }
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

