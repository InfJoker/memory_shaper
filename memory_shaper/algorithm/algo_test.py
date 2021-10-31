import pytest
from datetime import timedelta, datetime
import FlashCardAlgo


class TestAlgo:
    def test_count_time_before_next_show_false(self):
        f = FlashCardAlgo.FlashCardAlgorithm()
        prev_delta = f.current_delta
        time_d = f.count_time_before_next_show(False)
        assert(f.current_delta < prev_delta)
        assert(time_d == timedelta(minutes=2) or time_d == timedelta(minutes=f.current_delta * 10))

    def test_count_time_before_next_show_true(self):
        f = FlashCardAlgo.FlashCardAlgorithm()
        prev_delta = f.current_delta
        time_d = f.count_time_before_next_show(True)
        assert(f.current_delta > prev_delta)
        assert(time_d == timedelta(minutes=2) or time_d == timedelta(minutes=f.current_delta * 10))

    def test_reset_time(self):
        f = FlashCardAlgo.FlashCardAlgorithm()
        f.reset_time(True)
        assert(datetime.now() < f.next_show)