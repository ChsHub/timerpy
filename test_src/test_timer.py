from time import sleep

from hypothesis import given, settings
from hypothesis._strategies import floats
from hypothesis.strategies import text
from concurrent.futures import ThreadPoolExecutor

from timerpy.timer import Timer


def return_test(message, output):
    if message:
        assert output.startswith(message)

def run_timer(timeout):
    timeout, message = timeout
    # Run timer
    with Timer(message=message, log_function=lambda x: return_test(message, x)) as timer:
        sleep(timeout)
    return timer.elapsed_time

@settings(deadline=None)
@given(text(), floats(min_value=0.0, max_value=0.1))
def test_timer(message, timeout):

    repetitions = 100
    input = [(timeout, message)] * repetitions

    with ThreadPoolExecutor(max_workers=2) as executor:
        result = executor.map(run_timer, input)
        result = list(result)

    total_time = sum(result)

    assert abs(int(timeout * 1000000000 * repetitions) - total_time) < 5000000 * repetitions  # +/- Milliseconds accuracy


if __name__ == '__main__':
    test_timer()
