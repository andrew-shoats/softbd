import numpy as np
import point as pt
import spring as sp
import math

class Ball:

    def __init__(self, N_points, radius, mass):
        self._N_points = N_points
        self._N_springs = N_points - 1
        self._ball_points = np.empty(self._N_points, dtype=pt.Point)
        self._springs = np.empty(self._N_springs, dtype=sp.Spring)
        self._radius = radius
        self._mass = mass
        self._pressure_external = 100
        self._pressure = []

        self._create_points()
        self._volume = self._ball_volume()

    def _create_points(self):
        for idx in range(self._N_points):
            self._ball_points[idx] = pt.Point()
            self._ball_points[idx].x = self._radius * \
                np.sin(idx * (2.0 * np.pi) / self._N_points )
            self._ball_points[idx].y = self._radius * \
                np.cos(idx * (2.0 * np.pi) / self._N_points )

        for idx in range(self._N_springs):
            self._add_springs(idx,idx,idx+1)
            self._add_springs(idx-1,idx-1,1)

    def _add_springs(self, pi, i, j):

        self._springs[pi] = sp.Spring()
        self._springs[pi].i = i
        self._springs[pi].j = j
        self._springs[pi].length = self._calculate_spring_length(i, j)

    def _calculate_spring_length(self, i, j):

        return self.norm(
                self._ball_points[ i ].x, self._ball_points[ j ].x, \
                self._ball_points[ i ].y, self._ball_points[ j ].y)

    def _gravity_forces(self):

        for idx in range(self._N_points):
            self._ball_points[idx].fx = 0
            self._ball_points[idx].fy = self._mass * GRAVITY * (self._pressure - FINAL_PRESSURE >= 0)

    def _norm(self, x1, x2, y1, y2):
        return np.sqrt( \
                (x2 - x1) ** 2 + \
                (y2 - y1) ** 2)

    def _ball_volume(self):

        for idx in range(self._N_springs-1):
            x1 = self._ball_points[self._springs[idx].i].x
            y1 = self._ball_points[self._springs[idx].i].y
            x2 = self._ball_points[self._springs[idx].j].x
            y2 = self._ball_points[self._springs[idx].j].y

            r12d = self._norm(x1, x2, y1, y2)

            volume += 0.5 * math.fabs(x1 - x2) * math.fabs(self._springs[idx].nx) * r12d
#     /* Calculate Volume of the Ball

    def _calculate_pressure(self):

        for idx in range(self._N_springs-1):

            x1 = self._ball_points[self._springs[idx].i].x
            y1 = self._ball_points[self._springs[idx].i].y
            x2 = self._ball_points[self._springs[idx].j].x
            y2 = self._ball_points[self._springs[idx].j].y

            r12d = self._norm(x1, x2, y1, y2)

            pressure_rev = r12d * self._pressure_external * (1.0 / self._volume)


