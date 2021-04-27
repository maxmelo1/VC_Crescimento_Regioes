import numpy as np
import math

class Point(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y


def calcDissimilarity(img, p, q):
    return math.sqrt(img[p.x, p.y]**2 - img[q.x, q.y]**2)