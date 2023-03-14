import spacy
import uuid


class MySpacy:
    def __init__(self):
        self._nlp = spacy.load("en_core_web_sm")
        self._tasks = {}

    def sentences(self, data):
        res = []
        text = data['text']
        doc = self._nlp(text)
        for i, sent in enumerate(doc.sents):
            res.append({
                i+1: sent.text
            })
        return res

    def pos(self, data, query_params):
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
        return res

    def named_entities(self, data, task_id):
        self._add_task(task_id, "SUBMITTED")
        res = []
        text = data['text']
        doc = self._nlp(text)
        for ent in doc.ents:
            res.append(
                {
                    f"{ent.text}": f"{ent.label_}"
                }
            )
        return res

    def _add_task(self, task_id, state):
        self._tasks[task_id] = state

    def get_state(self, task_id):
        return self._tasks[task_id]