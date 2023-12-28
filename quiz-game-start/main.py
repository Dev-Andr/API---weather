from question_model import Question
from quiz_brain import QuizBrain
from ui import Interface
import requests

resp = requests.get(url='https://opentdb.com/api.php?amount=10&type=boolean')
resp.raise_for_status()
question_data = resp.json()['results']

qBank = []
for i in question_data:
    q = Question(i["question"], i["correct_answer"])
    qBank.append(q)


quiz_ui = Interface(QuizBrain(qBank))
