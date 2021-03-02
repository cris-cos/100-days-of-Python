#Functions with outputs
#Multiple return keywords


def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return "First name and last name were not provided"
    formatted_name = f_name.title() + " " + l_name.title()
    return formatted_name

print(format_name("crisTina", "cOsOroaba"))