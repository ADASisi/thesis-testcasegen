import gdspy
import basic_functions

lib = gdspy.GdsLibrary()

results = []


def display_test_cases(i, actual_enclosure, min_enclosure):
    if round(actual_enclosure, 3) < min_enclosure:
        return f"Test case {i + 1}: Enclosure area = {round(actual_enclosure, 3)} (Fail)"
    else:
        return f"Test case {i + 1}: Enclosure area = {round(actual_enclosure, 3)} (Pass)"


def export_file_minimum_enclosure(lib, first_layer_name, second_layer_name):
    gds_filename = f"{first_layer_name}_min_enclosure_{second_layer_name}_test.gds"
    lib.write_gds(gds_filename)
    print(f"GDS file '{gds_filename}' has been created.")


def display_file_minimum_enclosure(cell):
    gdspy.LayoutViewer(cells=cell)


def check_minimum_enclosure(min_enclosure, first_layer_name, second_layer_name, num_first_layer, num_second_layer,
                             first_datatype, second_datatype):
    global cell
    cell_name = f"{first_layer_name}_MIN_ENCLOSURE_{second_layer_name}_TEST"
    if basic_functions.cell_exists(lib, cell_name) is False:
        cell = lib.new_cell(cell_name)
        second_layer_specifications = basic_functions.get_layer_other_parameters(second_layer_name)
        width = second_layer_specifications["width"]
        height = width
        enclosure_areas = basic_functions.generate_value(min_enclosure)

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

            results.append(display_test_cases(i, actual_enclosure, min_enclosure))

    return results, lib, cell
