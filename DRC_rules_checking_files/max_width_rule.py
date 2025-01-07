import gdspy
import basic_functions

lib = gdspy.GdsLibrary()

results = []


def display_test_cases(i, actual_width, max_width):
    if round(actual_width, 3) > max_width:
        return f"Test case {i + 1}: Width = {round(actual_width, 3)} (Fail)"
    else:
        return f"Test case {i + 1}: Width = {round(actual_width, 3)} (Pass)"


def export_file_maximum_width(lib, layer_name):
    gds_filename = f"{layer_name}_max_width_test.gds"
    lib.write_gds(gds_filename)


def display_file_maximum_width(cell):
    gdspy.LayoutViewer(cells=cell)


def check_maximum_width(max_width, layer_name, num_layer, datatype):
    global cell
    cell_name = f"{layer_name}_MAX_WIDTH_TEST"
    if basic_functions.cell_exists(lib, cell_name) is False:

        cell = lib.new_cell(cell_name)

        widths = basic_functions.generate_value(max_width)

        for i, width in enumerate(widths):
            height = 7 #da go izmislq
            points = basic_functions.generate_polygon_points(basic_functions.base, basic_functions.base + i * width, width, height)
            polygon = gdspy.Polygon(points, layer=num_layer, datatype=datatype)
            cell.add(polygon)

            bounding_box = polygon.get_bounding_box()
            actual_width = bounding_box[1][0] - bounding_box[0][0]

            results.append(display_test_cases(i, actual_width, max_width))

    return results, lib, cell
