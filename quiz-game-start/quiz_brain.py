import html

class QuizBrain:
    def __init__(self, qna):
        self.qNo = 0
        self.score = 0
        self.qList = qna
        self.curQ = None

    def stillQ(self):
        if self.qNo < len(self.qList):
            return True

    def nextQ(self):
        self.curQ = self.qList[self.qNo]
        self.qNo += 1
        return f"Q.{self.qNo}: {html.unescape(self.curQ.text)}"

    def check(self, user_ans) -> str:
        if user_ans.lower() == self.curQ.ans.lower():
            self.score += 1
            return "green"
        else:
            return "red"
