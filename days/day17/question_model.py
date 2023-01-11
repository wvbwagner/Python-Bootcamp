class Question:

    def __init__(self, text, answer) -> None:
        self.text = text
        self.answer = answer

    def __str__(self) -> str:
        return f'{self.text}, {self.answer}'
        