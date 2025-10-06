import threading
class H2O:
    def __init__(self):
        self.sem_h = threading.Semaphore(2)
        self.sem_o = threading.Semaphore(0)
        self.lock_o = threading.Lock()
    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.sem_h.acquire()
        releaseHydrogen()
        self.sem_o.release()
    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.lock_o:
            self.sem_o.acquire()
            self.sem_o.acquire()
            releaseOxygen()
            self.sem_h.release()
            self.sem_h.release()