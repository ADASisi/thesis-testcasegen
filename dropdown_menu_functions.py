def get_rules_name():
    options_dropdown_menu = []
    with open("Resources/65LPe_V1830.psv", "r") as fpsv:
        for line in fpsv:
            split_text = line.strip().split("|")
            if len(split_text) > 2:
                options_dropdown_menu.append(split_text[2])
    return options_dropdown_menu


def show_rule_description(rule_name):
    description_rule = ""
    with open("Resources/65LPe_V1830.psv", "r") as fpsv:
        for line in fpsv:
            split_text = line.split("|")
            if split_text[2].strip() == rule_name:
                description_rule = split_text[4].strip() + split_text[5].strip() + split_text[6].strip()
                return description_rule
