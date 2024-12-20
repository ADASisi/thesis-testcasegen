import gdspy
import basic_functions

number_of_tests = 3

base = 1

lib = gdspy.GdsLibrary()

results = []


def display_test_cases(i, actual_enclosure, min_enclosure):
    if round(actual_enclosure, 3) < min_enclosure:
        return f"Test case {i + 1}: Enclosure area = {round(actual_enclosure, 3)} (Fail)"
    else:
        return f"Test case {i + 1}: Enclosure area = {round(actual_enclosure, 3)} (Pass)"


def export_file_minimum_width(lib, layer_name):
    gds_filename = f"{layer_name}_min_enclosure_test.gds"
    lib.write_gds(gds_filename)
    print(f"GDS file '{gds_filename}' has been created.")


def display_file_minimum_enclosure(cell):
    gdspy.LayoutViewer(cells=cell)


def check_min_enclosure_rule(min_enclosure, layer_name, num_layer, datatype):
    global cell
    cell_name = f"{layer_name}_MIN_ENCLOSURE_TEST"
    if basic_functions.cell_exists(lib, cell_name) is False:
        cell = lib.new_cell(cell_name)
        height = 0.08
        width = 0.08
        enclosure_areas = basic_functions.generate_value(min_enclosure)

        previous_x = base

        for i, enclosure_area in enumerate(enclosure_areas):
            x_offset = previous_x + i * 0.2

            points_polygon_1 = basic_functions.generate_polygon_points(x_offset, base, width, height)
            polygon_1 = gdspy.Polygon(points_polygon_1, layer=num_layer, datatype=datatype)
            cell.add(polygon_1)

            next_x = x_offset + enclosure_area

            points_polygon_2 = basic_functions.generate_polygon_points(
                next_x, base + enclosure_area, width - 2 * enclosure_area, height - 2 * enclosure_area
            )
            polygon_2 = gdspy.Polygon(points_polygon_2, layer=num_layer, datatype=datatype)
            cell.add(polygon_2)

            actual_enclosure = points_polygon_2[0][0] - points_polygon_1[0][0]

            results.append(display_test_cases(i, actual_enclosure, min_enclosure))

    return results, lib, cell
