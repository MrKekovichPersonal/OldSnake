import pygame
import random
from app.snake import Snake
from utilis.square import Square
from utilis.point import Point


class Game:
    HEIGHT = 30
    WIDTH = 40
    SCREEN_HEIGHT = HEIGHT * Square.SQUARE_TOTAL_SIDE_LENGTH
    SCREEN_WIDTH = WIDTH * Square.SQUARE_TOTAL_SIDE_LENGTH

    BACKGROUND_COLOR = "#ffffff"
    FOOD_COLOR = "#808000"

    PAUSE_TEXT = "Press Escape to unpause"
    GAME_OVER_TEXT = "Press Space to restart"

    def __init__(self, tick_rate: int = 5) -> None:
        pygame.init()
        self.__screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Snake!")
        self.__font = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.__clock = pygame.time.Clock()
        self.__active = True
        self.__reset()
        self.__tick_rate = tick_rate

    def __reset(self):
        self.__direction_key = None
        self.__snake = Snake(Point(self.WIDTH / 2, self.HEIGHT / 2), self)
        self.__generate_food()

    def __generate_food(self):
        self.__food = Square(
            self.FOOD_COLOR,
            Point(random.randrange(0, self.WIDTH), random.randrange(0, self.HEIGHT)),
        )

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if self.__snake.is_alive and event.key in Snake.DIRECTIONS:
                    self.__direction_key = event.key
                elif self.__snake.is_alive and event.key == pygame.K_ESCAPE:
                    self.__pause()
                elif not self.__snake.is_alive and event.key == pygame.K_SPACE:
                    self.__reset()

    def __tick(self):
        if self.__snake.is_alive:
            if self.__snake.move(self.__direction_key) == self.__food.position:
                self.__generate_food()
            else:
                self.__snake.shrink()

    def __draw(self):
        self.__screen.fill(pygame.Color(self.BACKGROUND_COLOR))

        if self.__snake.is_alive:
            self.__snake.draw(self.__screen)
            self.__food.draw(self.__screen)
        else:
            game_over = self.__font.render(self.GAME_OVER_TEXT, True, pygame.Color("#000000"))
            game_over_rect = game_over.get_rect(center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2))
            self.__screen.blit(game_over, game_over_rect)

        if not self.__active:
            pause = self.__font.render(self.PAUSE_TEXT, True, pygame.Color("#000000"))
            pause_rect = pause.get_rect(center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2))
            self.__screen.blit(pause, pause_rect)

        pygame.display.update()

    def __pause(self):
        self.__active = not self.__active

    def run(self):
        while True:
            pygame.time.delay(1 // self.__tick_rate)
            self.__clock.tick(self.__tick_rate)
            self.__handle_events()
            if self.__active:
                self.__tick()
            self.__draw()


if __name__ == "__main__":
    game = Game(7)  # Difficulty(speed) 7
    game.run()
