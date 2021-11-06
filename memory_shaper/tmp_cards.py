from queue import PriorityQueue

from algorithm.FlashCardAlgo import FlashCardAlgorithm


class FlashCard(FlashCardAlgorithm):
    def __init__(self, question: str, answer: str):
        super(FlashCard, self).__init__()
        self.question = question
        self.answer = answer


CARDS = [
    FlashCard(question='Bonjour', answer='Hello, Good morning'),
    FlashCard(question='Au revoir', answer='Goodbye'),
    FlashCard(question='Oui', answer='Yes'),
    FlashCard(question='Non', answer='No'),
    FlashCard(question='Merci', answer='Thank you'),
    FlashCard(question='Merci beaucoup', answer='Thank you very much'),
]


queue = PriorityQueue()


def init_queue():
    for i, card in enumerate(CARDS):
        queue.put((card.get_next_show_time(), i))


def get_queue():
    return queue
