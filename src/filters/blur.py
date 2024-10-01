import cv2
from filters.base import BaseFilter


class BlurFilter(BaseFilter):
    def process(self, frame):
        return cv2.GaussianBlur(frame, (19, 19), 0)
