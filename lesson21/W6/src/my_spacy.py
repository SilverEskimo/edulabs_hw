import uuid
import spacy
from threading import Lock


class MySpacy:
    def __init__(self):
        self._nlp = spacy.load("en_core_web_sm")
        self._update_lock = Lock()
        self._read_lock = Lock()
        self._tasks = {}
        self._completed_tasks = {}

    @staticmethod
    def update_task(function: callable) -> callable:
        def wrapping_function(*args, **kwargs):
            with args[0].get_update_lock():
                return function(*args, **kwargs)
        return wrapping_function

    @staticmethod
    def read_task(function: callable) -> callable:
        def wrapping_function(*args, **kwargs):
            with args[0].get_read_lock():
                return function(*args, **kwargs)
        return wrapping_function

    def sentences(self, data, task_id):
        self._add_task(task_id, "PROCESSING")
        res = []
        text = data['text']
        doc = self._nlp(text)
        for i, sent in enumerate(doc.sents):
            res.append({
                i+1: sent.text
            })
        self._update_task(res, task_id)

    def pos(self, data, query_params, task_id):
        self._add_task(task_id, "PROCESSING")
        tags = None
        res = []
        upper_tags = []
        if query_params:
            tags = query_params['tags'].split(",")
            for tag in tags:
                upper_tags.append(tag.upper())
        text = data['text']
        doc = self._nlp(text)
        for i, token in enumerate(doc):
            if not tags or (tags and token.pos_ in upper_tags):
                res.append(
                    {
                        f"{token.text.title()}":  token.pos_
                    }
                )
        self._update_task(res, task_id)

    def named_entities(self, data, task_id):
        self._add_task(task_id, "PROCESSING")
        res = []
        text = data['text']
        doc = self._nlp(text)
        for ent in doc.ents:
            res.append(
                {
                    f"{ent.text}": f"{ent.label_}"
                }
            )
        self._update_task(res, task_id)

    @update_task
    def _add_task(self, task_id, state):
        self._tasks[str(task_id)] = state

    @update_task
    def _update_task(self, result, task_id):
        self._tasks[str(task_id)] = "COMPLETED"
        self._completed_tasks[str(task_id)] = result

    @read_task
    def get_state(self, task_id):
        return self._tasks[task_id]

    @update_task
    def _delete_task(self, task_id):
        self._tasks.pop(task_id)
        self._completed_tasks.pop(task_id)

    def get_task(self, task_id):
        res = self._get_result(str(task_id))
        self._delete_task(str(task_id))
        return res

    @read_task
    def _get_result(self, task_id):
        return self._completed_tasks[task_id]

    @read_task
    def get_all_tasks(self):
        return self._tasks

    def get_read_lock(self):
        return self._read_lock

    def get_update_lock(self):
        return self._update_lock

    @staticmethod
    def generate_task_id():
        task_id = uuid.uuid4()
        res = {
            "task_id": task_id,
            "status": "SUBMITTED"
        }
        return res
