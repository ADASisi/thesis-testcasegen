import gdspy
import random
import basic_functions

number_of_tests = 3

base = 1


def display_test_cases(i, actual_area, min_area):
    if round(actual_area, 3) < min_area:
        return f"Test case {i + 1}: Area = {round(actual_area, 3)} (Fail)"
    else:
        return f"Test case {i + 1}: Area = {round(actual_area, 3)} (Pass)"


def export_file_minimum_area(lib, layer_name):
    gds_filename = f"{layer_name}_min_area_test.gds"
    lib.write_gds(gds_filename)


def display_file_minimum_area(cell):
    gdspy.LayoutViewer(cells=cell)


def check_minimum_area(min_area, layer_name, num_layer, datatype):
    lib = gdspy.GdsLibrary()
    cell_name = f"{layer_name}_MIN_AREA_TEST_{random.uniform(1,100)}"
    cell = lib.new_cell(cell_name)

    areas = basic_functions.generate_value(min_area)

    results = []

    for i, area in enumerate(areas):
        width = random.uniform(0.08, 0.1)
        height = area / width
        points = basic_functions.generate_polygon_points(base + i * 0.2, base, width, height)
        polygon = gdspy.Polygon(points, layer=num_layer, datatype=datatype)
        cell.add(polygon)
        actual_area = width * height

        results.append(display_test_cases(i, actual_area, min_area))

    return results, lib, cell
