import pyopencl as cl
import numpy as np


class Runner:
    def __init__(self, file: str, num_boids: int):
        self.context = cl.create_some_context(True)
        with open(file, 'r') as f:
            self.kernel = f.readlines()
        self.kernel = '\n'.join(self.kernel)
        self.prog = cl.Program(self.context, self.kernel).build(
            options=['-D NUM_BOIDS={}'.format(num_boids)])

    def run(self, bpos: np.ndarray) -> np.ndarray:
        with cl.CommandQueue(self.context) as q:
            mf = cl.mem_flags
            bpos_b = cl.Buffer(self.context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=bpos)
            res_b = cl.Buffer(self.context, mf.WRITE_ONLY, bpos.nbytes)
            self.prog.boid_kernel(q, bpos.shape, None, bpos_b, res_b)

            cl.enqueue_copy(q, bpos, res_b)

        return bpos
