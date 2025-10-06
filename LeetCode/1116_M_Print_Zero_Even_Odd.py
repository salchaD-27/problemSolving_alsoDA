import threading
from typing import Callable
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_sem = threading.Semaphore(1)  # zero önce başlasın
        self.even_sem = threading.Semaphore(0)
        self.odd_sem = threading.Semaphore(0)
    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.zero_sem.acquire()
            printNumber(0)
            if i % 2 == 0: self.even_sem.release()
            else: self.odd_sem.release()
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n+1, 2):
            self.even_sem.acquire()
            printNumber(i)
            self.zero_sem.release()
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1, 2):
            self.odd_sem.acquire()
            printNumber(i)
            self.zero_sem.release()