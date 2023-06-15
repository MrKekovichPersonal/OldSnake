import random
from utilis.point import Point
from utilis.square import Square
import pygame
from app.colors import ERainbowColor


class Snake:
    COLOR = "#7B68EE"
    DIRECTIONS = {
        pygame.K_UP: {"name": "up", "movement": Point(0, -1), "opposite": "down"},
        pygame.K_RIGHT: {"name": "right", "movement": Point(1, 0), "opposite": "left"},
        pygame.K_DOWN: {"name": "down", "movement": Point(0, 1), "opposite": "up"},
        pygame.K_LEFT: {"name": "left", "movement": Point(-1, 0), "opposite": "right"},
    }

    def __init__(
            self,
            position: Point,
            game,
    ) -> None:
        self.__squares = [Square(self.COLOR, position)]
        self.__direction = self.DIRECTIONS[pygame.K_RIGHT]
        self.is_alive = True
        self.game = game

    def move(self, key):
        if (
                key in self.DIRECTIONS and
                self.DIRECTIONS[key]["name"] != self.__direction["opposite"]
        ):
            self.__direction = self.DIRECTIONS[key]

        new_square = Square(
            self.random_color,
            self.__squares[-1].position + self.__direction["movement"]
        )

        if (
                new_square in self.__squares or
                new_square.position.x < 0 or
                new_square.position.x >= self.game.WIDTH or
                new_square.position.y < 0 or
                new_square.position.y >= self.game.HEIGHT
        ):
            self.is_alive = False

        self.__squares.append(new_square)
        return new_square.position

    def shrink(self):
        self.__squares.pop(0)

    def draw(self, surface: pygame.Surface):
        for square in self.__squares:
            square.draw(surface)

    @property
    def random_color(self):
        return random.choice(list(ERainbowColor)).value
