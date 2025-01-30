step = 0.001

base = 1


def generate_polygon_points(x, y, width, height):
    return [(x, y), (x + width, y), (x + width, y + height), (x, y + height)]


def generate_value(rule_val):
    return [rule_val - step, rule_val, rule_val + step]


def cell_exists(library, name):
    return name in library.cells


def get_layer_other_parameters(layer_name):
    layer_specifications = {'width': None, 'area': None, 'space': None}
    with open("Resources/65LPe_V1830.psv", "r") as fpsv:
        for line in fpsv:
            split_text = line.split("|")
            rule_parameters = split_text[4].strip().split()
            if layer_name == rule_parameters[0] and rule_parameters[1] in ("minimum", "exact"):
                layer_specifications[rule_parameters[2]] = float(split_text[6].strip())
    return layer_specifications
