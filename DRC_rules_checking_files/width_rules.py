import gdspy
import basic_functions

lib = gdspy.GdsLibrary()

results_min = []
results_exact = []


def display_test_cases(i, actual_width, rule_width, rule_type):
    actual_width = round(actual_width, 3)
    pass_fail = "Fail" if (
            (rule_type == "min" and actual_width < rule_width) or
            (rule_type == "exact" and actual_width != rule_width)
    ) else "Pass"
    return f"Test case {i + 1}: Width = {round(actual_width, 3)} ({pass_fail})"


def export_file_width_rule(lib, layer_name, rule_type):
    gds_filename = f"{layer_name}_{rule_type}_width_test.gds"
    lib.write_gds(gds_filename)


def display_file_width(cell):
    gdspy.LayoutViewer(cells=cell)


def check_width_rule(rule_width, layer_name, num_layer, datatype, rule_type):
    global cell
    cell_name = f"{layer_name}_{rule_type.upper()}_WIDTH_TEST"
    results = results_min if rule_type == "min" else results_exact

    if basic_functions.cell_exists(lib, cell_name) is False:
        cell = lib.new_cell(cell_name)

        widths = basic_functions.generate_value(rule_width)
        layer_specifications = basic_functions.get_layer_other_parameters(layer_name)

        for i, width in enumerate(widths):
            if layer_specifications["area"] is not None:
                height = layer_specifications["area"] / width
            else:
                height = width

            points = basic_functions.generate_polygon_points(basic_functions.base + i * width * 2, basic_functions.base,
                                                                 width, height)
            polygon = gdspy.Polygon(points, layer=num_layer, datatype=datatype)
            cell.add(polygon)

            bounding_box = polygon.get_bounding_box()
            actual_width = bounding_box[1][0] - bounding_box[0][0]

            results.append(display_test_cases(i, actual_width, rule_width, rule_type))

    return results, lib, cell


def check_minimum_width(min_width, layer_name, num_layer, datatype):
    return check_width_rule(min_width, layer_name, num_layer, datatype, rule_type="min")


def check_exact_width(exact_width, layer_name, num_layer, datatype):
    return check_width_rule(exact_width, layer_name, num_layer, datatype, rule_type="exact")