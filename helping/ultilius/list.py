def list(width: int, height: int, fill: str = '') -> list:
    world = []

    for _ in range(height):
        line = []
        for _ in range(width):
            line.append(fill)
        world.append(line)
    return world
