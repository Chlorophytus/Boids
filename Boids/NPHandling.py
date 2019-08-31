import numpy as np
import math


class BoidFactory:
    """This class constructs boids in the specified area."""

    def __init__(self, size: (int, int), num_boids: int):
        """
        Configure the factory.

        :param size: How large the viewport should be.
        """
        self.boids = np.random.random_sample((num_boids, 4))
        self.size = size
        self.num_boids = num_boids

    def __call__(self, *args, **kwargs) -> np.ndarray:
        """
        Call the factory, making an array of points to draw.

        :param args: 0 arguments.
        :param kwargs: 0 keyword arguments.
        :return: An array of points.
        """
        return self.render_boid_points()

    def render_boid_points(self) -> np.ndarray:
        """
        Renders an array of points.

        :return: The boids that are rendered.
        """

        return np.ndarray.astype(self.boids[0:2] * self.size % self.size, np.int)

    def render_boid_vectors(self):
        # FIXME
        return np.ndarray.astype(self.boids[2:4] * self.size % self.size, np.int)
