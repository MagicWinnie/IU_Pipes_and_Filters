from queue import Queue
from threading import Thread, Event

from custom_types import QueueType
from cv2.typing import MatLike


class BaseFilter(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.input_queue: QueueType = Queue()
        self.output_queue: QueueType = Queue()
        self.stop_event = Event()

    def run(self):
        while not self.stop_event.is_set():
            frame = self.input_queue.get()
            if frame is None:
                self.output_queue.put(frame)
                break
            processed_frame = self.process(frame)
            self.output_queue.put(processed_frame)

    def stop(self):
        self.stop_event.set()

    def process(self, frame: MatLike):
        ...
