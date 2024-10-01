import cv2
from threading import Thread
from custom_types import QueueType
from queue import Queue
from filters.hsv import HSVFilter
from filters.resize import ResizeFilter
from filters.mirror import MirrorFilter
from filters.blur import BlurFilter


ESCAPE = 27


def source(output_queue: QueueType, device: int = 0, window_name: str = "Source frame") -> None:
    cap = cv2.VideoCapture(device)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        output_queue.put(frame)

        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) == ESCAPE:
            break

    output_queue.put(None)

    cap.release()
    cv2.destroyWindow(window_name)


def sink(input_queue: QueueType, window_name: str = "Sink frame") -> None:
    while True:
        frame = input_queue.get()
        if frame is None:
            break

        cv2.imshow(window_name, frame)
        cv2.waitKey(1)  # can exit only from source

    cv2.destroyWindow(window_name)


def main(device: int = 0) -> None:
    source_queue: QueueType = Queue()
    sink_queue: QueueType = Queue()

    pipeline = [
        Thread(target=source, args=(source_queue, device)),
        ResizeFilter(),
        BlurFilter(),
        HSVFilter(),
        MirrorFilter(),
        Thread(target=sink, args=(sink_queue,)),
    ]

    pipeline[1].input_queue = source_queue
    pipeline[2].input_queue = pipeline[1].output_queue
    pipeline[3].input_queue = pipeline[2].output_queue
    pipeline[4].input_queue = pipeline[3].output_queue
    pipeline[4].output_queue = sink_queue

    for pipeline_thread in pipeline:
        pipeline_thread.start()

    for pipeline_thread in pipeline:
        pipeline_thread.join()


if __name__ == "__main__":
    main()
