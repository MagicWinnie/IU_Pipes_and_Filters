import cv2
from queue import Queue

QueueType = Queue[cv2.typing.MatLike | None]
