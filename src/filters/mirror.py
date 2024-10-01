import cv2
from filters.base import BaseFilter


class MirrorFilter(BaseFilter):
    def process(self, frame):
        return cv2.flip(frame, 0)
