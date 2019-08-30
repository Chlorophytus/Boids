#!/usr/bin/env python3.7
from Boids import Boids
import sdl2

def main():
    window = Boids.Window((800, 600))
    window.handler.run()

if __name__ == '__main__':
    main()