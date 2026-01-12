from utils.number_emoji import NUMBER_EMOJI
from utils.console_utils import print_section, print_warning, print_info


def run_menu(menu_dict, extra_info=None):
    """
    Displays a menu, validates user input, and returns the selected key.
    Uses console_utils for standardized output.

    Args:
        menu_dict (dict): Menu dictionary with 'title' and 'options'
        extra_info (str, optional): Extra info to display above menu options

    Returns:
        int: The selected menu option key
    """
    while True:
        # Print section header
        print_section(menu_dict["title"])

        # Print extra info if available
        if extra_info:
            print_info(extra_info)

        # Print menu options
        for opt in menu_dict["options"]:
            emoji_key = NUMBER_EMOJI.get(opt["key"], str(opt["key"]))
            print(f"{emoji_key} {opt['label']}")

        # Get user input
        choice = input("Choose an option: ")

        # Validate input is a number
        if not choice.isdigit():
            print_warning("Please enter a number!")
            continue

        choice = int(choice)
        valid_keys = [opt["key"] for opt in menu_dict["options"]]

        # Validate choice is in valid keys
        if choice not in valid_keys:
            print_warning(f"Invalid option. Choose from {valid_keys}")
            continue

        return choice
