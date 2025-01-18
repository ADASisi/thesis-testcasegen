import importlib
import os
import sys

sys.path.append(os.path.join(os.getcwd(), "DRC_rules_checking_files"))

func = {}

for file in os.listdir("DRC_rules_checking_files"):
    if file.endswith(".py") and file != "__init__.py":
        module_name = file[:-3]
        module = importlib.import_module(module_name)
        for attr in dir(module):
            attr_value = getattr(module, attr)
            if callable(attr_value):
                func[attr] = attr_value


def construct_function_name(parameter_1, parameter_2):
    func_name = "check_"
    if parameter_1 == "minimum":
        func_name += "minimum_"
    elif parameter_1 == "maximum":
        func_name += "maximum_"
    if parameter_2 == "width":
        func_name += "width"
    elif parameter_2 == "area":
        func_name += "area"
    elif parameter_2 == "space":
        func_name += "space"
    elif parameter_2 == "enclosure":
        func_name += "enclosure"
    elif parameter_2 == "overlap_of":
        func_name += "overlap_of"
    elif parameter_2 == "overlap_past":
        func_name += "overlap_past"
    return func_name


def call_function_by_name(function_name, *args):
    if function_name in func:
        return func[function_name](*args)
    else:
        return [f"Function {function_name} not found or is not callable."]


def get_rule_parameters(rule_name):
    def parse_map_file(map_file):
        mapping = {}
        with open(map_file, "r") as fmap:
            for line in fmap:
                fields = line.split()
                mapping[fields[2].strip()] = (int(fields[0]), int(fields[1]))
        return mapping

    map_data = parse_map_file("Resources/65LPe.map")

    def build_result(parm_1, parm_2, number, layer_name, map_data, second_layer_name=None):
        if layer_name in map_data:
            number_layer, datatype = map_data[layer_name]
            if second_layer_name:
                if second_layer_name in map_data:
                    second_layer_number, second_datatype = map_data[second_layer_name]
                    return {
                        "parm_1": parm_1,
                        "parm_2": parm_2,
                        "number": number,
                        "layer_name": layer_name,
                        "number_layer": number_layer,
                        "number_datatype": datatype,
                        "second_layer_name": second_layer_name,
                        "second_layer_number": second_layer_number,
                        "second_datatype": second_datatype,
                    }
            else:
                return {
                    "parm_1": parm_1,
                    "parm_2": parm_2,
                    "number": number,
                    "layer_name": layer_name,
                    "number_layer": number_layer,
                    "number_datatype": datatype,
                }
        return {"error": f"Layer {layer_name} or {second_layer_name} not found in map data."}

    with open("Resources/65LPe_V1830.psv", "r") as fpsv:
        for line in fpsv:
            split_text = line.split("|")
            if split_text[2].strip() == rule_name:
                rule_parameters = split_text[4].strip().split()
                number = float(split_text[6].strip())
                layer_name = rule_parameters[0]
                parm_1 = rule_parameters[1]
                parm_2 = rule_parameters[2]

                if parm_2 == "overlap":
                    parm_3 = rule_parameters[3]
                    parm_2 = parm_2 + "_" + parm_3
                    second_layer_name = rule_parameters[4]
                    return build_result(parm_1, parm_2, number, layer_name, map_data, second_layer_name)
                if parm_2 == "enclosure":
                    second_layer_name = rule_parameters[3]
                    return build_result(parm_1, parm_2, number, layer_name, map_data, second_layer_name)
                else:
                    return build_result(parm_1, parm_2, number, layer_name, map_data)

    return {"error": f"Rule number {rule_name} doesn't exist."}


def rule_displaying(rule_name):
    rule_data = get_rule_parameters(rule_name)

    if "error" in rule_data:
        return rule_data["error"]

    parm_1 = rule_data["parm_1"]
    parm_2 = rule_data["parm_2"]
    number = rule_data["number"]
    layer_name = rule_data["layer_name"]
    number_layer = rule_data["number_layer"]
    number_datatype = rule_data["number_datatype"]

    function_name = construct_function_name(parm_1, parm_2)

    if parm_2 == "overlap_past" or parm_2 == "overlap_of" or parm_2 == "enclosure":
        second_layer_name = rule_data["second_layer_name"]
        second_layer_number = rule_data["second_layer_number"]
        second_datatype = rule_data["second_datatype"]

        results, lib, cell = call_function_by_name(
            function_name, number, layer_name, second_layer_name,
            number_layer, second_layer_number, number_datatype, second_datatype
        )
    else:
        results, lib, cell = call_function_by_name(
            function_name, number, layer_name, number_layer, number_datatype
        )

    call_function_by_name(f"display_file_{parm_1}_{parm_2}", cell)

    return results, layer_name, lib, parm_1, parm_2


def export_file(rule_name):
    rule_data = get_rule_parameters(rule_name)

    if "error" in rule_data:
        return rule_data["error"]

    parm_1 = rule_data["parm_1"]
    parm_2 = rule_data["parm_2"]
    number = rule_data["number"]
    layer_name = rule_data["layer_name"]
    number_layer = rule_data["number_layer"]
    number_datatype = rule_data["number_datatype"]

    function_name = construct_function_name(parm_1, parm_2)

    if parm_2 == "overlap_past" or parm_2 == "overlap_of" or parm_2 == "enclosure":
        second_layer_name = rule_data["second_layer_name"]
        second_layer_number = rule_data["second_layer_number"]
        second_datatype = rule_data["second_datatype"]

        results, lib, cell = call_function_by_name(
            function_name, number, layer_name, second_layer_name,
            number_layer, second_layer_number, number_datatype, second_datatype
        )
        call_function_by_name(f"export_file_{parm_1}_{parm_2}", lib, layer_name, second_layer_name)

    else:
        results, lib, cell = call_function_by_name(
            function_name, number, layer_name, number_layer, number_datatype
        )
        call_function_by_name(f"export_file_{parm_1}_{parm_2}", lib, layer_name)

    return results
