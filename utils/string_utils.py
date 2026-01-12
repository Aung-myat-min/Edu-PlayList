import re

def clean_input(user_input: str) -> str:
    """
    Cleans user input by:
        - Removing leading and trailing spaces
        - Replacing multiple spaces between words with a single space

    Args:
        user_input (str): Raw string from user

    Returns:
        str: Cleaned string
    """
    if not isinstance(user_input, str):
        return ""

    # Strip leading/trailing spaces
    cleaned = user_input.strip()

    # Replace multiple consecutive spaces with a single space
    cleaned = re.sub(r"\s+", " ", cleaned)

    return cleaned
