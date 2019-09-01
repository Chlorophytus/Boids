import sdl2
import sdl2.ext
import numpy as np
from typing import Callable


class Window:
    def __init__(self, size: (int, int), callback: Callable[[object, int], np.ndarray] = None):
        sdl2.ext.init()
        self.size = size
        self.window = sdl2.ext.Window("Boids!", size)
        self.render = sdl2.ext.Renderer(self.window)
        self.window.show()
        self.handler = EventHandler(self.window, self.render, callback)


class EventHandler:
    def __init__(self, window: sdl2.ext.Window, renderer: sdl2.ext.Renderer,
                 callback: Callable[[object, int], np.ndarray] = None):
        self.running = False
        self.window = window
        self.renderer = renderer
        self.callback = callback
        self.point_cloud = None

    def run(self):
        self.running = True
        while self.running:
            self.renderer.clear()
            if self.callback is not None:
                self.point_cloud = self.callback()
                self.renderer.draw_point(np.reshape(self.point_cloud, self.point_cloud.size), sdl2.ext.Color())
            self.renderer.present()
            self.window.refresh()
            sdl2.SDL_Delay(1000 // 120)
            for i in sdl2.ext.get_events():
                if i.type == sdl2.SDL_QUIT:
                    sdl2.ext.quit()
                    self.running = False
