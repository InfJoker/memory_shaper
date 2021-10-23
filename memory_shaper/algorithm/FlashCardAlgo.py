from datetime import datetime, timedelta


class FlashCardAlgorithm:
    def __init__(self):
        self.current_delta = 1
        self.number_of_showings = 0
        self.number_of_correct_ans = 0
        self.next_show = datetime.now() + timedelta(minutes=10)

    def count_time_before_next_show(self, correct: bool) -> timedelta:
        if correct:
            self.number_of_correct_ans += 1
        percentage_of_corr_ans = self.number_of_correct_ans / self.number_of_showings
        if correct:
            self.current_delta += 0.5 * percentage_of_corr_ans * self.number_of_showings
        else:
            self.current_delta -= 0.2 * (1 - percentage_of_corr_ans) * self.number_of_showings
        return timedelta(minutes=max(10 * self.current_delta, 2))

    def reset_time(self, correct: bool):
        self.number_of_showings += 1
        self.next_show = datetime.now() + self.count_time_before_next_show(correct)

    def get_next_show_time(self) -> datetime:
        return self.next_show


def get_modified_card(elem: FlashCardAlgorithm, correct: bool) -> FlashCardAlgorithm:
    elem.reset_time(correct)
    return elem
