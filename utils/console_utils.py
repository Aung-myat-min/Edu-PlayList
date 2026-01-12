import os
import time
import sys
from colorama import init, Fore, Style
from tabulate import tabulate

# Initialize colorama
init(autoreset=True)

# ---------------- Colors & Symbols ----------------
SUCCESS = Fore.GREEN + "✅"
ERROR = Fore.RED + "❌"
WARNING = Fore.YELLOW + "⚠️"
INFO = Fore.CYAN + "ℹ️"

# ---------------- Configuration ----------------
PRINT_DELAY = 0.01  # Seconds to wait after each print for "smoothness"

def _slow_print(text, end="\n"):
    """Internal helper to print text and then sleep slightly."""
    print(text, end=end)
    if PRINT_DELAY > 0:
        time.sleep(PRINT_DELAY)

# def clear_screen():
#     """Clears the console screen."""
#     os.system('cls' if os.name == 'nt' else 'clear')

# ---------------- Messages ----------------
def print_success(message):
    _slow_print(f"{SUCCESS} {message}")


def print_error(message):
    _slow_print(f"{ERROR} {message}")


def print_warning(message):
    _slow_print(f"{WARNING} {message}")


def print_info(message):
    _slow_print(f"{INFO} {message}")


# ---------------- Tables ----------------
def print_table(data, headers=None, tablefmt="fancy_grid"):
    """
    Prints a list of dictionaries or list of lists as a table.

    Args:
        data (list): List of dicts or lists to display.
        headers (list): Column headers if data is list of lists.
        tablefmt (str): Tabulate format (default: fancy_grid)
    """
    if not data:
        print_warning("No data available.")
        return

    # If data is list of dicts, use keys as headers
    if isinstance(data[0], dict):
        _slow_print(tabulate(data, headers="keys", tablefmt=tablefmt))
    else:
        _slow_print(tabulate(data, headers=headers, tablefmt=tablefmt))


# ---------------- Section Headers ----------------
def print_section(title, width=50):
    """
    Clears screen, prints a section header with lines and centers the title.

    Args:
        title (str): The section title
        width (int): Total width of the section
    """
    # clear_screen()
    _slow_print("=" * width)
    _slow_print(Style.BRIGHT + title.center(width))
    _slow_print("=" * width)


# ---------------- Extra Info ----------------
def print_extra_info(info):
    """
    Prints extra info (like tries left or login status)
    """
    _slow_print(f"{INFO} {info}")
    _slow_print("-" * 50)
