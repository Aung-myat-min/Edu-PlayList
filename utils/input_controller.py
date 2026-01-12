from utils.string_utils import clean_input
from utils.console_utils import print_warning

def get_valid_input(prompt: str, min_len: int = 3) -> str:
    """
    Gets validated user input with minimum length.
    """
    while True:
        value = clean_input(input(prompt))

        if len(value) < min_len:
            print_warning(f"Input must be at least {min_len} characters.")
            continue

        return value
