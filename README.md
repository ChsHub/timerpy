# timerpy
Measure execution time of code sections.

## Installation
`python3 -m pip install timerpy`

## Usage Examples
Default usage
```python

from timerpy import Timer
with Timer():
    # Some code

>>>TIME ELAPSED: 0:00:01.199748
´´´
Specify a message
```python
with Timer('HELLO WORLD'):
    # Some code

>>>HELLO WORLD TIME ELAPSED: 0:02:15.242731
´´´
Specify output
```python
from logging import info # Write to log file
with Timer('HELLO WORLD', info):
    # Some code

>>>timer.py: INFO: stop(): 44:	HELLO WORLD TIME ELAPSED: 0:00:01.200157
´´´
Get elapsed time as float value
```python
with Timer() as timer1:
    # Some code
seconds = timer1.elapsed_time
print(seconds)

>>>TIME ELAPSED: 0:00:01.399406
>>>1.3994057
```