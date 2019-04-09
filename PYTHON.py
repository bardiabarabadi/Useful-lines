

# This is useful for measuring the elapsed time
from contextlib import contextmanager
@contextmanager
def timer(op_string, will_print=False):
    start_time = -time.time()
    fileobj = open('printed.txt', 'w')
    try:
        yield fileobj
    finally:
        total_time = 1000 * (time.time() + start_time)
        if will_print: print("{0:.<40}{1:.>15}".format('[TIME: ' + op_string + ']',
                                                     ' {:4.2f}'.format(total_time) + ' ms'))

# Sometimes no print is best print
@contextmanager
def no_print():
    old = sys.stdout
    fileobj = open('printed.txt', 'w')
    sys.stdout = fileobj
    try:
        yield fileobj
    finally:
        sys.stdout = old
        os.remove('printed.txt')


