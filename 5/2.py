class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius
    
    def get_radius(self) -> float:
        return self.radius
    
    def set_radius(self, new_radius: float) -> None:
        self.radius = new_radius


def main():
    circle = Circle(5)

    print(f"Радиус круга: {circle.get_radius()}")

    circle.set_radius(228)

    print(f"Новый радиус круга: {circle.get_radius()}")


if __name__ == "__main__":
    main()
