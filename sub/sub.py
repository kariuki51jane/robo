class behaviours(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.paused = False
        self.pause_cond = threading.Condition(threading.Lock())

    def run(self):
        while True:
            with self.pause_cond:
                while self.paused:
                    self.pause_cond.wait()
                print 'do the thing'
            time.sleep(5)

    def pause(self):
        self.paused = True
        self.pause_cond.acquire()

    def resume(self):
        self.paused = False
        self.pause_cond.notify()
        self.pause_cond.release()


thread1=behaviours()
