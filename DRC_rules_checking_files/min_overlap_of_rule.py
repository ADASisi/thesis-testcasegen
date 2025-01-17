import gdspy
import basic_functions

lib = gdspy.GdsLibrary()

results = []


def display_test_cases(i, actual_overlap, min_overlap):
    if round(actual_overlap, 3) < min_overlap:
        return f"Test case {i + 1}: Overlap = {round(actual_overlap, 3)} (Fail)"
    else:
        return f"Test case {i + 1}: Overlap = {round(actual_overlap, 3)} (Pass)"


def export_file_minimum_overlap_of(lib, first_layer_name, second_layer_name):
    gds_filename = f"min_{first_layer_name}_overlap_of_{second_layer_name}_test.gds"
    lib.write_gds(gds_filename)


def display_file_minimum_overlap_of(cell):
    gdspy.LayoutViewer(cells=cell)


def check_minimum_overlap_of(min_overlap, first_layer_name, second_layer_name, num_first_layer, num_second_layer,
                             first_datatype, second_datatype):
    global cell
    cell_name = f"MIN_{first_layer_name}_OVERLAP_OF_{second_layer_name}_TEST"
    if basic_functions.cell_exists(lib, cell_name) is False:
        cell = lib.new_cell(cell_name)

        first_layer_specifications = basic_functions.get_layer_other_parameters(first_layer_name)
        big_width = first_layer_specifications["width"]
        if first_layer_specifications["area"] is not None:
            big_height = first_layer_specifications["area"] / big_width
        else:
            big_height = big_width / 2

        overlaps = basic_functions.generate_value(min_overlap)

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

            results.append(display_test_cases(i, actual_overlap, min_overlap))

    return results, lib, cell
    # gdspy.LayoutViewer()

# check_minimum_overlap_of(1, "T3", "NW", 1, 2, 3, 3)
