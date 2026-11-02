from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    SPEED = 6

    def __init__(self, x, y, direction):
        self.x, self.y = x, y
        self.direction = direction
        self.image = load_image('ball21x21.png')

    def update(self):
        self.x += self.direction * self.SPEED
        if self.is_offscreen():
            game_world.remove_object(self)

    def is_offscreen(self):
        return self.x < -20 or self.x > get_canvas_width() + 20

    def draw(self):
        self.image.draw(self.x, self.y)
