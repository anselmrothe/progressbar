import time, sys

class ProgressBar:
    def __init__(self, n_or_list, barLength = 40):
        if isinstance(n_or_list, int) or isinstance(n_or_list, float):
            self.n = int(n_or_list)
        else:
            self.n = len(n_or_list)
        self.i = 0
        self.barLength = barLength
        self.start_time = time.mktime(time.gmtime())
    def next(self):
        self.i += 1.0
        progress = self.i / self.n
        self.paint(progress)
    def paint(self, progress):
        seconds_passed = time.mktime(time.gmtime()) - self.start_time
        average = seconds_passed / self.i
        seconds_remaining = (self.n - self.i) * average
        nbars = int(round(self.barLength * progress))
        bar = '|%s|' % ("="*nbars + " "*(self.barLength - nbars))
        percent = '%s%%' % int(progress*100)
        if self.i < self.n:
            time_remaining = '~%s remaining' % format_time(seconds_remaining)
        elif self.i == self.n:
            time_remaining = 'Completed after %s\n' % format_time(seconds_passed)
        elif self.i > self.n:
            time_remaining = '[i>n] Running time %s' % format_time(seconds_passed)
        text = "\r{0} {1} {2}".format(bar, percent, time_remaining)
        sys.stdout.write(text)
        sys.stdout.flush()
    def complete(self):
        self.n = self.i
        progress = self.i / self.n
        self.paint(progress)
        
def format_time(sec):
    if sec < 60:
        return str(int(sec)) + 's'
    if sec < (60 * 60):
        return str(round(sec/60, 1)) + 'm'
    else:
        return str(round(sec/60/60, 1)) + 'h'

if __name__ == '__main__':
    ## init via integer
    p = ProgressBar(100)
    for i in range(100):
        time.sleep(.02)
        p.next()

    ## init via size of list
    x = ['number' + str(x) for x in range(100)]
    p = ProgressBar(x)
    for i in x:
        time.sleep(.02)
        p.next()
