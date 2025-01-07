import gdspy
import basic_functions

lib = gdspy.GdsLibrary()

results = []


def display_test_cases(i, actual_overlap, min_overlap):
    if round(actual_overlap, 3) < min_overlap:
        return f"Test case {i + 1}: Overlap = {round(actual_overlap, 3)} (Fail)"
    else:
        return f"Test case {i + 1}: Overlap = {round(actual_overlap, 3)} (Pass)"


def export_file_minimum_overlapof(lib, layer_name):
    gds_filename = f"min_overlap_of_{layer_name}_test.gds"
    lib.write_gds(gds_filename)


def display_file_minimum_overlapof(cell):
    gdspy.LayoutViewer(cells=cell)


def check_min_overlapof_rule(min_overlap, layer_name, num_layer, datatype):
    global cell
    cell_name = f"MIN_OVERLAP_OF_{layer_name}_TEST"
    if basic_functions.cell_exists(lib, cell_name) is False:
        cell = lib.new_cell(cell_name)
        height = 0.08
        width = 0.04
        overlaps = basic_functions.generate_value(min_overlap)

        previous_x = basic_functions.base

        for i, overlap in enumerate(overlaps):
            x_offset = previous_x + i * 0.2

            big_polygon_points = basic_functions.generate_polygon_points(
                x_offset, basic_functions.base, width, height
            )
            polygon_1 = gdspy.Polygon(big_polygon_points, layer=num_layer, datatype=datatype)
            cell.add(polygon_1)

            next_x = x_offset - overlap

            small_polygon_points = basic_functions.generate_polygon_points(
                next_x, basic_functions.base + overlap / 2,  overlap * 2, height - overlap
            )
            polygon_2 = gdspy.Polygon(small_polygon_points, layer=num_layer, datatype=datatype)
            cell.add(polygon_2)

            actual_overlap = small_polygon_points[1][0] - big_polygon_points[0][0]

            results.append(display_test_cases(i, actual_overlap, min_overlap))

    return results, lib, cell
