import gdspy
import basic_functions

lib = gdspy.GdsLibrary()

results_min = []


def display_test_cases(i, actual_overlap, rule_overlap, rule_type):
    actual_overlap = round(actual_overlap, 3)
    pass_fail = "Fail" if (
        (rule_type == "min" and actual_overlap < rule_overlap)
    ) else "Pass"
    return f"Test case {i + 1}: Space = {actual_overlap} ({pass_fail})"


def export_file_space_rule(lib, layer_name, rule_type):
    gds_filename = f"{layer_name}_{rule_type}_space_test.gds"
    lib.write_gds(gds_filename)


def display_file_space(cell):
    gdspy.LayoutViewer(cells=cell)


def check_space_rule(min_space, layer_name, num_layer, datatype, rule_type):
    global cell
    cell_name = f"{layer_name}_{rule_type.upper()}_SPACE_TEST"
    results = results_min if rule_type == "min" else results_min

    if basic_functions.cell_exists(lib, cell_name) is False:
        cell = lib.new_cell(cell_name)

        spaces = basic_functions.generate_value(min_space)

        layer_specifications = basic_functions.get_layer_other_parameters(layer_name)
        width = layer_specifications["width"]
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

            results.append(display_test_cases(i, actual_space, min_space, rule_type))

            previous_x = next_x + width + min_space

    return results, lib, cell


def check_minimum_space(min_space, layer_name, num_layer, datatype):
    return check_space_rule(min_space, layer_name, num_layer, datatype, rule_type="min")


# def check_maximum_space(max_space, layer_name, num_layer, datatype):
#     return check_space_rule(max_space, layer_name, num_layer, datatype, rule_type="max")
