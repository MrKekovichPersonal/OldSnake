class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other) -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other) -> "Point":
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other) -> "Point":
        return Point(self.x * other.x, self.y * other.y)

    def __truediv__(self, other) -> "Point":
        return Point(self.x / other.x, self.y / other.y)

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other) -> bool:
        return self.x != other.x or self.y != other.y

    def __lt__(self, other) -> bool:
        return self.x < other.x and self.y < other.y

    def __gt__(self, other) -> bool:
        return self.x > other.x and self.y > other.y

    def __le__(self, other) -> bool:
        return self.x <= other.x and self.y <= other.y

    def __ge__(self, other) -> bool:
        return self.x >= other.x and self.y >= other.y

    @property
    def position(self) -> tuple:
        return (self.x, self.y)

    def set_position(self, x=None, y=None) -> None:
        self.x = x or self.x
        self.y = y or self.y