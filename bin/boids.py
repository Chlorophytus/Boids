#!/usr/bin/env python3.7
from Boids import SDLHandling, NPHandling, Compute

SIZE = (640, 480)
NUM_BOIDS = 4096

def main():
    boid_kernel = Compute.Runner("bin/boid.cl", NUM_BOIDS)
    boids = NPHandling.BoidFactory(SIZE, NUM_BOIDS, boid_kernel)
    window = SDLHandling.Window(SIZE, boids)
    window.handler.run()


if __name__ == '__main__':
    main()