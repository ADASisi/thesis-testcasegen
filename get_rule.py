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
            if callable(getattr(module, attr)):
                func[attr] = getattr(module, attr)


def construct_function_name(parameter_1, parameter_2):
    func_name = "check_"
    if parameter_1 == "minimum":
        func_name = func_name + "minimum_"
    elif parameter_1 == "maximum":
        func_name = func_name + "maximum_"
    if parameter_2 == "width":
        func_name = func_name + "width"
    elif parameter_2 == "area":
        func_name = func_name + "area"
    elif parameter_2 == "space":
        func_name = func_name + "space"
    return func_name


def call_function_by_name(function_name, *args):
    if function_name in func:
        return func[function_name](*args)
    else:
        return [f"Function {function_name} not found or is not callable."]


def export_file(rule_name):
    rule_data = get_rule_name(rule_name)
    # if isinstance(rule_data, str):
    #     raise ValueError(rule_data)
    parm_1, parm_2, number, layer_name, number_layer, number_datatype = rule_data
    function_name = construct_function_name(parm_1, parm_2)
    results, lib = call_function_by_name(function_name, number, layer_name, number_layer, number_datatype)
    call_function_by_name(f"export_file_{rule_data[0]}_{rule_data[1]}", lib, layer_name)


def get_rule_name(rule_name):
    with open("65LPe_V1830.psv", "r") as fpsv:
        for line in fpsv:
            split_text = line.split("|")
            if split_text[2].strip() == rule_name:
                rule_parameters = split_text[4].strip().split()
                number = float(split_text[6].strip())
                layer_name = rule_parameters[0]
                parm_1 = rule_parameters[1]
                parm_2 = rule_parameters[2]
                with open("65LPe.map", "r") as fmap:
                    for map_line in fmap:
                        map_text = map_line.split()
                        if layer_name == map_text[2].strip():
                            number_layer = int(map_text[0])
                            number_datatype = int(map_text[1])
                            return parm_1, parm_2, number, layer_name, number_layer, number_datatype
    return [f"Rule number {rule_name} doesn't exist."]


def rule_displaying(rule_name):
    parm_1, parm_2, number, layer_name, number_layer, number_datatype = get_rule_name(rule_name)
    function_name = construct_function_name(parm_1, parm_2)
    results, lib = call_function_by_name(function_name, number, layer_name, number_layer, number_datatype)
    call_function_by_name(f"display_file_{parm_1}_{parm_2}")
    return results, layer_name, lib, parm_1, parm_2
