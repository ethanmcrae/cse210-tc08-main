class Score():

    def __init__(self):
        self._score = 0

    def add_scores(self, score):

        self._score += score
        return self._score

