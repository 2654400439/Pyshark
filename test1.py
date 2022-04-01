import time
from func_timeout import func_set_timeout
import func_timeout


@func_set_timeout(3)
def mytest():
    time.sleep(10)
    return 5


if __name__ == '__main__':
    mytest()
