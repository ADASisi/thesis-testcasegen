import gdspy
import random
import basic_functions

lib = gdspy.GdsLibrary()

results = []


def display_test_cases(i, actual_space, min_space):
    if round(actual_space, 3) < min_space:
        return f"Test case {i + 1}: Space = {round(actual_space, 3)} (Fail)"
    else:
        return f"Test case {i + 1}: Space = {round(actual_space, 3)} (Pass)"


def export_file_minimum_space(lib, layer_name):
    gds_filename = f"{layer_name}_min_space_test.gds"
    lib.write_gds(gds_filename)


def display_file_minimum_space(cell):
    gdspy.LayoutViewer(cells=cell)


def check_minimum_space(min_space, layer_name, num_layer, datatype):
    global cell
    cell_name = f"{layer_name}_MIN_SPACE_TEST"
    if basic_functions.cell_exists(lib, cell_name) is False:
        cell = lib.new_cell(cell_name)
        spaces = basic_functions.generate_value(min_space)
        width = random.uniform(0.1, 0.5)
        height = width

        previous_x = basic_functions.base

        for i, space in enumerate(spaces):
            points1 = basic_functions.generate_polygon_points(previous_x, basic_functions.base, width, height)
            polygon1 = gdspy.Polygon(points1, layer=num_layer, datatype=datatype)
            cell.add(polygon1)

            next_x = previous_x + width + space

            points2 = basic_functions.generate_polygon_points(next_x, basic_functions.base, width, height)
            polygon2 = gdspy.Polygon(points2, layer=num_layer, datatype=datatype)
            cell.add(polygon2)

            actual_space = points2[0][0] - points1[1][0]

            results.append(display_test_cases(i, actual_space, min_space))

            previous_x = next_x + width + min_space

    return results, lib, cell
