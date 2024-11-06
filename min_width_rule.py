import gdspy
import random

step = 0.001

number_of_tests = 3

base = 1


def generate_polygon_points(x, y, width, height):
    return [(x, y), (x + width, y), (x + width, y + height), (x, y + height)]


def generate_value(rule_val):
    return [rule_val - step, rule_val, rule_val + step]

def check_minimum_width(min_width, layer_name, num_layer, datatype):
    lib = gdspy.GdsLibrary()
    cell = lib.new_cell(layer_name + "_MIN_WIDTH_TEST")

    widths = generate_value(min_width)

    for i, width in enumerate(widths):
        height = random.uniform(1, 3)
        points = generate_polygon_points(base + i * 0.2, base, width, height)
        polygon = gdspy.Polygon(points, layer=num_layer, datatype=datatype)
        cell.add(polygon)

        bounding_box = polygon.get_bounding_box()
        actual_width = bounding_box[1][0] - bounding_box[0][0]

        if round(actual_width, 3) < min_width:
            print(f"Test case {i + 1}: Width = {actual_width} (Fail)")
        else:
            print(f"Test case {i + 1}: Width = {actual_width} (Pass)")

    lib.write_gds(layer_name + '_min_width_test.gds')