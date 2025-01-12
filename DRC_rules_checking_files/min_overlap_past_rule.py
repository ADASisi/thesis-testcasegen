import gdspy
import basic_functions

lib = gdspy.GdsLibrary()

results = []


def display_test_cases(i, actual_overlap, min_overlap):
    if round(actual_overlap, 3) < min_overlap:
        return f"Test case {i + 1}: Overlap = {round(actual_overlap, 3)} (Fail)"
    else:
        return f"Test case {i + 1}: Overlap = {round(actual_overlap, 3)} (Pass)"


def export_file_minimum_overlap_past(lib, layer_name):
    gds_filename = f"min_overlap_past_{layer_name}_test.gds"
    lib.write_gds(gds_filename)


def display_file_minimum_overlap_past(cell):
    gdspy.LayoutViewer(cells=cell)


def check_minimum_overlap_past(min_overlap, inside_layer_name, outside_layer_name, num_inside_layer, num_outside_layer, inside_datatype, outside_datatype):
    global cell
    cell_name = f"MIN_{inside_layer_name}_OVERLAP_PAST_{outside_layer_name}_TEST"
    if basic_functions.cell_exists(lib, cell_name) is False:
        cell = lib.new_cell(cell_name)
        height = 8
        width = 4
        overlaps = basic_functions.generate_value(min_overlap)

        previous_x = basic_functions.base

        for i, overlap in enumerate(overlaps):
            x_offset = previous_x + i * 10 + overlap

            small_polygon_points = basic_functions.generate_polygon_points(
                x_offset, basic_functions.base + overlap / 2, width - overlap / 2, height - overlap
            )
            polygon_1 = gdspy.Polygon(small_polygon_points, layer=num_outside_layer, datatype=outside_datatype)
            cell.add(polygon_1)

            next_x = x_offset - overlap

            big_polygon_points = basic_functions.generate_polygon_points(
                next_x, basic_functions.base, width, height
            )
            polygon_2 = gdspy.Polygon(big_polygon_points, layer=num_inside_layer, datatype=inside_datatype)
            cell.add(polygon_2)

            actual_overlap = small_polygon_points[0][0] - big_polygon_points[0][0]

            results.append(display_test_cases(i, actual_overlap, min_overlap))

    return results, lib, cell
    # gdspy.LayoutViewer()

# check_minimum_overlap_past(0.02, "K", "J", 1, 2, 3, 1)
