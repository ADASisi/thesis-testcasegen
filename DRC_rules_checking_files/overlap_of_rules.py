import gdspy
import basic_functions

lib = gdspy.GdsLibrary()

results_min = []


def display_test_cases(i, actual_overlap, rule_overlap, rule_type):
    actual_overlap = round(actual_overlap, 3)
    pass_fail = "Fail" if (
        (rule_type == "min" and actual_overlap < rule_overlap)
    ) else "Pass"
    return f"Test case {i + 1}: Overlap = {actual_overlap} ({pass_fail})"


def export_file_overlap_of_rule(lib, first_layer_name, second_layer_name, rule_type):
    gds_filename = f"{rule_type}_{first_layer_name}_overlap_of_{second_layer_name}_test.gds"
    lib.write_gds(gds_filename)


def display_file_overlap_of(cell):
    gdspy.LayoutViewer(cells=cell)


def check_overlap_of(rule_overlap, first_layer_name, second_layer_name, num_first_layer, num_second_layer,
                     first_datatype, second_datatype, rule_type):
    global cell
    cell_name = f"{rule_type.upper()}_{first_layer_name}_OVERLAP_OF_{second_layer_name}_TEST"
    results = results_min if rule_type == "min" else results_min

    if basic_functions.cell_exists(lib, cell_name) is False:
        cell = lib.new_cell(cell_name)

        first_layer_specifications = basic_functions.get_layer_other_parameters(first_layer_name)
        big_width = first_layer_specifications["width"]
        if first_layer_specifications["area"] is not None:
            big_height = first_layer_specifications["area"] / big_width
        else:
            big_height = big_width / 2

        overlaps = basic_functions.generate_value(rule_overlap)

        previous_x = basic_functions.base

        for i, overlap in enumerate(overlaps):
            x_offset = previous_x + i * first_layer_specifications["space"] * 2

            big_polygon_points = basic_functions.generate_polygon_points(
                x_offset, basic_functions.base, big_width, big_height
            )
            polygon_1 = gdspy.Polygon(big_polygon_points, layer=num_first_layer, datatype=first_datatype)
            cell.add(polygon_1)

            next_x = x_offset - overlap

            small_polygon_points = basic_functions.generate_polygon_points(
                next_x, basic_functions.base + overlap / 2, overlap * 2, big_height - overlap
            )
            polygon_2 = gdspy.Polygon(small_polygon_points, layer=num_second_layer, datatype=second_datatype)
            cell.add(polygon_2)

            actual_overlap = small_polygon_points[1][0] - big_polygon_points[0][0]

            results.append(display_test_cases(i, actual_overlap, rule_overlap, rule_type))

    return results, lib, cell


def check_minimum_overlap_of(min_overlap, inside_layer_name, outside_layer_name, num_inside_layer, num_outside_layer,
                             inside_datatype, outside_datatype):
    return check_overlap_of(min_overlap, inside_layer_name, outside_layer_name, num_inside_layer, num_outside_layer,
                            inside_datatype, outside_datatype, rule_type="min")
