import cv2
from filters.base import BaseFilter


class HSVFilter(BaseFilter):
    def process(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
