import gdspy
import random
import basic_functions

number_of_tests = 3

base = 1


def display_test_cases(i, actual_width, min_width):
    if round(actual_width, 3) < min_width:
        return f"Test case {i + 1}: Space = {actual_width} (Fail)"
    else:
        return f"Test case {i + 1}: Space = {actual_width} (Pass)"


def check_minimum_width(min_width, layer_name, num_layer, datatype):
    lib = gdspy.GdsLibrary()
    cell = lib.new_cell(layer_name + "_MIN_WIDTH_TEST")

    widths = basic_functions.generate_value(min_width)
    results = []

    for i, width in enumerate(widths):
        height = random.uniform(1, 3)
        points = basic_functions.generate_polygon_points(base + i * 0.2, base, width, height)
        polygon = gdspy.Polygon(points, layer=num_layer, datatype=datatype)
        cell.add(polygon)

        bounding_box = polygon.get_bounding_box()
        actual_width = bounding_box[1][0] - bounding_box[0][0]

        results.append(display_test_cases(i, actual_width, min_width))


    lib.write_gds(layer_name + '_min_width_test.gds')
    gdspy.LayoutViewer()
    return results