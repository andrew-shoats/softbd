import numpy as np

class Spring:

    def __init__(self, points_list, length, normal_vec):

        self._points_list = points_list
        self._length = length
        self._normal_vec = normal_vec