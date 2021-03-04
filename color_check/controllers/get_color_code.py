# This file should contain a function called get_color_code().
# This function should take one argument, a color name,
# and it should return one argument, the hex code of the color,
# if that color exists in our data. If it does not exist, you should
# raise and handle an error that helps both you as a developer,
# for example by logging the request and error, and the user,
# letting them know that their color doesn't exist.
import json



with open("color_check/data/css-color-names.json", "r") as read_file:
    dict_of_colors = json.load(read_file)




def get_color_code(color_name):
    if color_name in dict_of_colors:
        hex_code = dict_of_colors.get(color_name)
        return hex_code
    else:
        return "sorry this is not a CSS code"

def get_color_name(color_input):
    if color_input in dict_of_colors:
        current_color_name = color_input
        return current_color_name
    else:
        return "not a CSS color"
    # this is where you should add your logic to check the color.
    # Open the file at data/css-color-names.json, and return the hex code
    # The file can be considered as JSON format, or as a Python dictionary.