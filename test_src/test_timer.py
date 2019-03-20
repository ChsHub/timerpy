from time import sleep

from hypothesis import given
from hypothesis.strategies import text

from src.timer import Timer


@given(text())
def test_timer(message):
    with Timer(message=message):
        sleep(0.1)


if __name__ == '__main__':
    test_timer()