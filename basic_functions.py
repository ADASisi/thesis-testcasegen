step = 0.001


def generate_polygon_points(x, y, width, height):
    return [(x, y), (x + width, y), (x + width, y + height), (x, y + height)]


def generate_value(rule_val):
    return [rule_val - step, rule_val, rule_val + step]