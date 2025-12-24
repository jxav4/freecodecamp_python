#** start of main.py **

def add_setting(set_dict, key_value_pair):
    key = key_value_pair[0].lower()
    value = key_value_pair[1].lower()

    if key in set_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        set_dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(set_dict, key_value_pair):
    key = key_value_pair[0].lower()
    value = key_value_pair[1].lower()

    if key in set_dict:
        set_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(set_dict, keys):
    key = keys.lower()

    if key in set_dict:
        del set_dict[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(set_dict):
    if not set_dict:
        return f"No settings available."
    else:
        result = "Current User Settings:\n"
        for key, value in set_dict.items():
            result += f"{key.capitalize()}: {value}\n"
        return result

test_settings = {
    'theme': 'light',
    'contrast': 'normal',
    'volume': 'low'
} 

#** end of main.py **

