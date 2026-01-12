from utils.string_utils import clean_input
from utils.console_utils import print_warning


def get_valid_input(prompt: str, min_len: int = 3, default: str = None) -> str:
    """
    Gets validated user input with minimum length.

    Args:
        prompt (str): Prompt message for input.
        min_len (int): Minimum length required for input.
        default (str, optional): Default value to return if user enters 'n' or just presses Enter.

    Returns:
        str: Cleaned and validated user input or the default value.
    """
    while True:
        value = clean_input(input(prompt))

        # Use default if user enters 'n' or empty string and default is provided
        if default is not None and (value.lower() == 'n' or value == ''):
            return default

        if len(value) < min_len:
            print_warning(f"Input must be at least {min_len} characters.")
            continue

        return value
