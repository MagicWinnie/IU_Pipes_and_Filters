import cv2
from threading import Thread
from custom_types import QueueType
from filters.resize import ResizeFilter


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
    resize_thread = ResizeFilter()

    source_thread = Thread(target=source, args=(resize_thread.input_queue, device))
    sink_thread = Thread(target=sink, args=(resize_thread.output_queue,))

    source_thread.start()
    resize_thread.start()
    sink_thread.start()

    source_thread.join()
    resize_thread.join()
    sink_thread.join()


if __name__ == "__main__":
    main()
