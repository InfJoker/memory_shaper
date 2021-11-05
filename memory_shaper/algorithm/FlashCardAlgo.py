from datetime import datetime, timedelta


class FlashCardAlgorithm:
    def __init__(self, delta, n_of_showings, n_of_correct_ans):
        self.current_delta = delta
        self.number_of_showings = n_of_showings
        self.number_of_correct_ans = n_of_correct_ans
        self.next_show = datetime.now()

    def count_time_before_next_show(self, correct: bool) -> timedelta:
        self.number_of_showings += 1
        if correct:
            self.number_of_correct_ans += 1
        if correct:
            self.current_delta += 0.5 * self.number_of_correct_ans
        else:
            self.current_delta -= 0.2 * (self.number_of_showings - self.number_of_correct_ans)
        return timedelta(minutes=max(10 * self.current_delta, 2))

    def reset_time(self, correct: bool):
        self.next_show = datetime.now() + self.count_time_before_next_show(correct)

    def get_next_show_time(self) -> datetime:
        return self.next_show


def get_modified_card(elem: FlashCardAlgorithm, correct: bool) -> FlashCardAlgorithm:
    elem.reset_time(correct)
    return elem
