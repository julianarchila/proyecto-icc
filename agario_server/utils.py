import uuid, random, math


def generate_id() -> str:
    new_id = uuid.uuid4()
    return str(new_id)


def calc_distance(x1, y1, x2, y2):

    diffX = math.fabs(x1 - x2)
    diffY = math.fabs(y1 - y2)
    return ((diffX**2) + (diffY**2)) ** (0.5)

def generate_random_color() -> tuple:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
