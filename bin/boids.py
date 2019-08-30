#!/usr/bin/env python3.7
from Boids import SDLHandling

def main():
    window = SDLHandling.Window((800, 600))
    window.handler.run()

if __name__ == '__main__':
    main()