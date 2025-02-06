import gdspy
import basic_functions

lib = gdspy.GdsLibrary()

results_min = {}
results_max = {}


def display_test_cases(i, actual_area, rule_area, rule_type):
    pass_fail = "Fail" if (
            (rule_type == "min" and actual_area < rule_area) or
            (rule_type == "max" and actual_area > rule_area)
    ) else "Pass"
    return f"Test case {i + 1}: Area = {round(actual_area, 3)} ({pass_fail})"


def export_file_area_rule(lib, layer_name, rule_type):
    gds_filename = f"{layer_name}_{rule_type}_area_test.gds"
    lib.write_gds(gds_filename)


def display_file_area(cell):
    gdspy.LayoutViewer(cells=cell)


def check_area_rule(rule_area, layer_name, num_layer, datatype, rule_type):
    global cell
    cell_name = f"{layer_name}_{rule_type.upper()}_AREA_TEST"
    results = results_min if rule_type == "min" else results_max

    results.setdefault(layer_name, [])

    if basic_functions.cell_exists(lib, cell_name) is False:
        cell = lib.new_cell(cell_name)

        areas = basic_functions.generate_value(rule_area)
        layer_specifications = basic_functions.get_layer_other_parameters(layer_name)
        width = layer_specifications["width"]

        for i, area in enumerate(areas):
            height = area / width

            points = basic_functions.generate_polygon_points(
                basic_functions.base + i * width * 2, basic_functions.base, width, height
            )
            polygon = gdspy.Polygon(points, layer=num_layer, datatype=datatype)
            cell.add(polygon)

            actual_area = width * height

            results[layer_name].append(display_test_cases(i, actual_area, rule_area, rule_type))

    else:
        cell = lib.cells[cell_name]

    return results[layer_name], lib, cell


def check_minimum_area(min_area, layer_name, num_layer, datatype):
    return check_area_rule(min_area, layer_name, num_layer, datatype, rule_type="min")


def check_maximum_area(max_area, layer_name, num_layer, datatype):
    return check_area_rule(max_area, layer_name, num_layer, datatype, rule_type="max")