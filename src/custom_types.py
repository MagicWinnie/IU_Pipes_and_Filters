from queue import Queue

import cv2

QueueType = Queue[cv2.typing.MatLike | None]
