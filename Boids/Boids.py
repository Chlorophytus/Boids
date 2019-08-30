import numpy as np
import sdl2
import sdl2.ext


class Window:
    def __init__(self, size: (int, int)):
        sdl2.ext.init()
        self.size = size
        self.window = sdl2.ext.Window("Boids!", size)
        self.render = sdl2.ext.Renderer(self.window)
        self.window.show()
        self.handler = EventHandler(self.window, self.render)


class EventHandler:
    def __init__(self, window: sdl2.ext.Window, renderer: sdl2.ext.Renderer, cb):
        self.running = False
        self.window = window
        self.renderer = renderer
        self.render_cb

    def run(self):
        self.running = True
        while self.running:
            self.renderer.present()
            self.window.refresh()
            for i in sdl2.ext.get_events():
                if i.type == sdl2.SDL_QUIT:
                    print("bye")
                    sdl2.ext.quit()
                    self.running = False
