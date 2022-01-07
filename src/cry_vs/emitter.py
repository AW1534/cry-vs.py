import queue

class Emitter:
    q = queue.Queue()

    def __init__(self,
                 funcs,
                 expire,
                 events=[
                     "any_event",
                     "on_ready"
                 ],
                 ):
        self.funcs = funcs
        self.events = events

    def queue(self):
        while True:
            if self.q.empty(): continue
            curr = self.q.get()
            for func in self.funcs:
                if func.__name__ in self.events and func.__name__ == curr[0].lower():
                    try:
                        func(*curr[1])
                    except TypeError:
                        func()

    def enqueue(self, name, args=[]):
        self.q.put(item=[name, args])