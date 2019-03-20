from timeit import default_timer
from logging import info


class Timer:
    _info = None
    exe_time = None

    def __init__(self, message='', log=True):
        if not type(message) == str:
            raise TypeError
        self._message = message + ' '
        if log:
            self._info = info
        else:
            self._info = print

    def __enter__(self):
        self._start = default_timer() # Use default timer for maximum accuracy

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exe_time = default_timer() - self._start
        self._info('%s TIME ELAPSED: %s s' % (self._message, str(self.exe_time)))
