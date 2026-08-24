from circleshape import CircleShape as cs

class Asteroid(cs):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)