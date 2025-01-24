import gdspy
import basic_functions

lib = gdspy.GdsLibrary()

results_min = []
results_exact = []


def display_test_cases(i, actual_overlap, rule_overlap, rule_type):
    actual_overlap = round(actual_overlap, 3)
    pass_fail = "Fail" if (
            (rule_type == "min" and actual_overlap < rule_overlap) or
            (rule_type == "exact" and actual_overlap != rule_overlap)
    ) else "Pass"
    return f"Test case {i + 1}: Overlap = {actual_overlap} ({pass_fail})"


def export_file_overlap_past_rule(lib, inside_layer_name, outside_layer_name, rule_type):
    gds_filename = f"{rule_type}_{inside_layer_name}_overlap_past_{outside_layer_name}_test.gds"
    lib.write_gds(gds_filename)


def display_file_overlap_past(cell):
    gdspy.LayoutViewer(cells=cell)


def check_overlap_past(rule_overlap, inside_layer_name, outside_layer_name, num_inside_layer, num_outside_layer,
                       inside_datatype, outside_datatype, rule_type):
    global cell
    cell_name = f"{rule_type.upper()}_{inside_layer_name}_OVERLAP_PAST_{outside_layer_name}_TEST"
    results = results_min if rule_type == "min" else results_exact

    if basic_functions.cell_exists(lib, cell_name) is False:
        cell = lib.new_cell(cell_name)

        outside_layer_specifications = basic_functions.get_layer_other_parameters(outside_layer_name)
        big_width = outside_layer_specifications["width"]
        if big_width < rule_overlap:
            big_width = rule_overlap * 3
            big_height = big_width / 2

        else:
            if outside_layer_specifications["area"] is not None:
                big_height = outside_layer_specifications["area"] / big_width
            else:
                big_height = big_width / 2

        print(big_width)
        overlaps = basic_functions.generate_value(rule_overlap)

        previous_x = basic_functions.base

        for i, overlap in enumerate(overlaps):
            x_offset = previous_x + i * big_width * 2

            small_polygon_points = basic_functions.generate_polygon_points(
                x_offset, basic_functions.base + overlap / 2, big_width - overlap / 2, big_height - overlap
            )
            polygon_1 = gdspy.Polygon(small_polygon_points, layer=num_outside_layer, datatype=outside_datatype)
            cell.add(polygon_1)

            next_x = x_offset - overlap

            big_polygon_points = basic_functions.generate_polygon_points(
                next_x, basic_functions.base, big_width, big_height
            )
            polygon_2 = gdspy.Polygon(big_polygon_points, layer=num_inside_layer, datatype=inside_datatype)
            cell.add(polygon_2)

            actual_overlap = small_polygon_points[0][0] - big_polygon_points[0][0]

            results.append(display_test_cases(i, actual_overlap, rule_overlap, rule_type))

    return results, lib, cell


def check_minimum_overlap_past(min_overlap, inside_layer_name, outside_layer_name, num_inside_layer, num_outside_layer,
                               inside_datatype, outside_datatype):
    return check_overlap_past(min_overlap, inside_layer_name, outside_layer_name, num_inside_layer, num_outside_layer,
                              inside_datatype, outside_datatype, rule_type="min")


def check_exact_overlap_past(exact_overlap, inside_layer_name, outside_layer_name, num_inside_layer, num_outside_layer,
                             inside_datatype, outside_datatype):
    return check_overlap_past(exact_overlap, inside_layer_name, outside_layer_name, num_inside_layer, num_outside_layer,
                              inside_datatype, outside_datatype, rule_type="exact")
