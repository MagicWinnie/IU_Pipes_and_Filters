import cv2
from filters.base import BaseFilter


class ResizeFilter(BaseFilter):
    def process(self, frame):
        return cv2.resize(frame, (500, 500))
