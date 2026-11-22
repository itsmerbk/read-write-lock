import threading

class RWLock:
    def __init__(self): self.cond, self.readers, self.writer = threading.Condition(), 0, False
    def acquire_read(self):
        with self.cond:
            while self.writer: self.cond.wait()
            self.readers += 1
    def release_read(self):
        with self.cond:
            self.readers -= 1
            if self.readers == 0: self.cond.notify_all()
    def acquire_write(self):
        with self.cond:
            while self.writer or self.readers > 0: self.cond.wait()
            self.writer = True
    def release_write(self):
        with self.cond: self.writer = False; self.cond.notify_all()

if __name__ == "__main__":
    rw = RWLock(); rw.acquire_read(); rw.acquire_read(); rw.release_read(); rw.release_read()
    rw.acquire_write(); rw.release_write()
    print("[PASS] 062_read_write_lock")
