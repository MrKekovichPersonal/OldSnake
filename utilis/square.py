from utilis.point import Point
import pygame


class Square:
    SQUARE_BORDER_WIDTH = 1
    SQUARE_SIDE_LENGTH = 10
    SQUARE_TOTAL_SIDE_LENGTH = (
            SQUARE_SIDE_LENGTH + SQUARE_BORDER_WIDTH * 2
    )

    def __init__(self, color: str, position: Point) -> None:
        self.__color = color
        self.position = position

    def __eq__(self, other: "Square") -> bool:
        return self.position == other.position

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(
            surface,
            self.__color,
            (
                self.position.x * self.SQUARE_TOTAL_SIDE_LENGTH + self.SQUARE_BORDER_WIDTH,
                self.position.y * self.SQUARE_TOTAL_SIDE_LENGTH + self.SQUARE_BORDER_WIDTH,
                self.SQUARE_SIDE_LENGTH,
                self.SQUARE_SIDE_LENGTH,
            )
        )
