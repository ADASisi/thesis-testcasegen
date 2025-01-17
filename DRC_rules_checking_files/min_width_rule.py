import gdspy
import random
import basic_functions

lib = gdspy.GdsLibrary()

results = []


def display_test_cases(i, actual_width, min_width):
    if round(actual_width, 3) < min_width:
        return f"Test case {i + 1}: Width = {round(actual_width, 3)} (Fail)"
    else:
        return f"Test case {i + 1}: Width = {round(actual_width, 3)} (Pass)"


def export_file_minimum_width(lib, layer_name):
    gds_filename = f"{layer_name}_min_width_test.gds"
    lib.write_gds(gds_filename)
    print(f"GDS file '{gds_filename}' has been created.")


def display_file_minimum_width(cell):
    gdspy.LayoutViewer(cells=cell)


def check_minimum_width(min_width, layer_name, num_layer, datatype):
    global cell
    cell_name = f"{layer_name}_MIN_WIDTH_TEST"
    if basic_functions.cell_exists(lib, cell_name) is False:
        cell = lib.new_cell(cell_name)

        widths = basic_functions.generate_value(min_width)

        for i, width in enumerate(widths):
            layer_specifications = basic_functions.get_layer_other_parameters(layer_name)
            if layer_specifications["area"] is not None:
                height = layer_specifications["area"] / width
            else:
                height = width
            # if layer_specifications["space"] is not None:
            #     points = basic_functions.generate_polygon_points(
            #         basic_functions.base + layer_specifications["space"] + i * width, basic_functions.base, width, height)
            # else:
            points = basic_functions.generate_polygon_points(basic_functions.base + i * width * 2, basic_functions.base,
                                                                 width, height)
            polygon = gdspy.Polygon(points, layer=num_layer, datatype=datatype)
            cell.add(polygon)

            bounding_box = polygon.get_bounding_box()
            actual_width = bounding_box[1][0] - bounding_box[0][0]

            results.append(display_test_cases(i, actual_width, min_width))

    return results, lib, cell
    # gdspy.LayoutViewer()

# check_minimum_width(0.1, "M2", 1, 2)