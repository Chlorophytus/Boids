import pyopencl as cl
import numpy as np


class Runner:
    def __init__(self, file: str, num_boids: int):
        self.context = cl.create_some_context(True)
        with open(file, 'r') as f:
            self.kernel = f.readlines()
        print(self.kernel)
        self.kernel = '\n'.join(self.kernel)
        self.k_bin = cl.Program(self.context, self.kernel).build(
            options=['-D NUM_BOIDS={}'.format(num_boids)])

    def run(self):
        print("pass")
        pass
