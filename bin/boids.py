#!/usr/bin/env python3.7
from Boids import SDLHandling, NPHandling, Compute

SIZE = (1600, 900)
NUM_BOIDS = 512

def main():
    boid_kernel = Compute.Runner("bin/boid.cl", NUM_BOIDS)
    boids = NPHandling.BoidFactory(SIZE, NUM_BOIDS)
    window = SDLHandling.Window(SIZE, boids)
    window.handler.run()


if __name__ == '__main__':
    main()