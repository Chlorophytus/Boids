import pyopencl as cl
import numpy as np


class Runner:
    def __init__(self):
        self.context = cl.create_some_context(True)
        self.queue = cl.CommandQueue(self.context)

    def run(self):
