import uuid
from src.my_spacy import MySpacy
from flask import Flask, request, jsonify
from concurrent.futures import ThreadPoolExecutor


app = Flask("NLP_WEB_Server")
my_spacy = MySpacy()
executor = ThreadPoolExecutor()


@app.route("/api/v1/sentences", methods=['POST'])
def sentences():
    res = my_spacy.generate_task_id()
    executor.submit(my_spacy.sentences, request.form, res["task_id"])
    return jsonify(res)


@app.route("/api/v1/pos", methods=['POST'])
def pos():
    res = my_spacy.generate_task_id()
    query_params = request.args if request.args else None
    executor.submit(my_spacy.pos, request.form, query_params, res["task_id"])
    return jsonify(res)


@app.route("/api/v1/named_ents", methods=['POST'])
def named_entities():
    res = my_spacy.generate_task_id()
    executor.submit(my_spacy.named_entities, request.form, res["task_id"])
    return jsonify(res)


@app.route("/api/v1/tasks/<task_id>/status", methods=['GET'])
def get_status(task_id):
    return jsonify(
        {
            "status": my_spacy.get_state(task_id)
        }
    )


@app.route("/api/v1/tasks/<task_id>/result", methods=['GET'])
def get_result(task_id):
    return jsonify(my_spacy.get_task(task_id))


@app.route("/api/v1/tasks", methods=['GET'])
def get_tasks():
    return jsonify(my_spacy.get_all_tasks())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

