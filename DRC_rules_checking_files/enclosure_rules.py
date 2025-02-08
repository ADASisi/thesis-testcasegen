import gdspy
import basic_functions

lib = gdspy.GdsLibrary()

results_min_enclosure = []


def display_test_cases(i, actual_enclosure, rule_enclosure, rule_type):
    actual_enclosure = round(actual_enclosure, 3)
    pass_fail = "Fail" if (
        (rule_type == "min" and actual_enclosure < rule_enclosure)
    ) else "Pass"
    return f"Test case {i + 1}: Enclosure area = {actual_enclosure} ({pass_fail})"


def export_file_enclosure_rule(lib, first_layer_name, second_layer_name, rule_type):
    gds_filename = f"{first_layer_name}_{rule_type}_enclosure_{second_layer_name}_test.gds"
    lib.write_gds(gds_filename)


def display_file_enclosure(cell):
    gdspy.LayoutViewer(cells=cell, pattern={'default': 5}, background='#FFFFFF')


def check_enclosure_rule(rule_enclosure, first_layer_name, second_layer_name, num_first_layer, num_second_layer,
                    first_datatype, second_datatype, rule_type):
    global cell
    cell_name = f"{rule_type.upper()}_{first_layer_name}_ENCLOSURE_{second_layer_name}_TEST"
    results = results_min_enclosure if rule_type == "min" else results_min_enclosure

    if basic_functions.cell_exists(lib, cell_name) is False:
        cell = lib.new_cell(cell_name)

        second_layer_specifications = basic_functions.get_layer_other_parameters(second_layer_name)
        width = second_layer_specifications["width"]
        height = width

        enclosure_areas = basic_functions.generate_value(rule_enclosure)

        previous_x = basic_functions.base

        for i, enclosure_area in enumerate(enclosure_areas):
            x_offset = previous_x + i * 0.2

            points_polygon_1 = basic_functions.generate_polygon_points(x_offset, basic_functions.base, width, height)
            polygon_1 = gdspy.Polygon(points_polygon_1, layer=num_first_layer, datatype=first_datatype)
            cell.add(polygon_1)

            next_x = x_offset + enclosure_area

            points_polygon_2 = basic_functions.generate_polygon_points(
                next_x, basic_functions.base + enclosure_area, width - 2 * enclosure_area, height - 2 * enclosure_area
            )
            polygon_2 = gdspy.Polygon(points_polygon_2, layer=num_second_layer, datatype=second_datatype)
            cell.add(polygon_2)

            actual_enclosure = points_polygon_2[0][0] - points_polygon_1[0][0]

            results.append(display_test_cases(i, actual_enclosure, rule_enclosure, rule_type))

    else:
        cell = lib.cells[cell_name]

    return results, lib, cell


def check_minimum_enclosure(min_enclosure, first_layer_name, second_layer_name, num_first_layer, num_second_layer,
                               first_datatype, second_datatype):
    return check_enclosure_rule(min_enclosure, first_layer_name, second_layer_name, num_first_layer, num_second_layer,
                              first_datatype, second_datatype, rule_type="min")
