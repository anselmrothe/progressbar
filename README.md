# progressbar
progressbar for python

inspired by the phenomenal tidyverse progress bar

```python
from progressbar import ProgressBar

## init via integer
p = ProgressBar(100)
for i in range(100):
    time.sleep(.02)
    p.next()
# |========================================| 100% Completed after 2s

## init via size of list
x = ['number' + str(x) for x in range(100)]
p = ProgressBar(x)
for i in x:
    time.sleep(.02)
    p.next()
# |========================================| 100% Completed after 2s
```
