import random
import gdspy
import basic_functions

number_of_tests = 3

base = 1


def display_test_cases(i, actual_width, max_width):
    if round(actual_width, 3) < max_width:
        return f"Test case {i + 1}: Width = {round(actual_width, 3)} (Fail)"
    else:
        return f"Test case {i + 1}: Width = {round(actual_width, 3)} (Pass)"


def export_file_maximum_width(lib, layer_name):
    gds_filename = f"{layer_name}_max_width_test.gds"
    lib.write_gds(gds_filename)


def display_file_maximum_width():
    gdspy.LayoutViewer()


def check_maximum_width(max_width, layer_name, num_layer, datatype):
    lib = gdspy.GdsLibrary()
    cell_name = f"{layer_name}_MAX_WIDTH_TEST_{random.uniform(1,100)}"
    cell = lib.new_cell(cell_name)

    widths = basic_functions.generate_value(max_width)

    results = []

    for i, width in enumerate(widths):
        height = random.uniform(1, 3)
        points = basic_functions.generate_polygon_points(base, base + i * width, width, height)
        polygon = gdspy.Polygon(points, layer=num_layer, datatype=datatype)
        cell.add(polygon)

        bounding_box = polygon.get_bounding_box()
        actual_width = bounding_box[1][0] - bounding_box[0][0]

        results.append(display_test_cases(i, actual_width, max_width))

    return results, lib
