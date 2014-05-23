from __future__ import division


from datetime import datetime

from .printing import print_info,print_success

__all__ = ["Timer"]

class Timer(object):
    def __init__(self,n_iters,iter_size=0.05):
        self.n_iters = n_iters
        self.iter_size = iter_size
        self._counter = 0
        self._p_done = 0.0

    def tick(self):
        if self._counter == 0:
            self._start = datetime.now()
        self._counter += 1
        if (self._counter / self.n_iters) > self._p_done:
            print_info("%3d percent done" % (100 * self._p_done,))
            self._p_done += self.iter_size
        if self._counter == self.n_iters:
            print_success("All done!")

    def reset(self):
        self._counter = 0
        self._p_done = 0.0
