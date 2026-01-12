from colorama import init, Fore, Style
from tabulate import tabulate

# Initialize colorama
init(autoreset=True)

# ---------------- Colors & Symbols ----------------
SUCCESS = Fore.GREEN + "✅"
ERROR = Fore.RED + "❌"
WARNING = Fore.YELLOW + "⚠️"
INFO = Fore.CYAN + "ℹ️"


# ---------------- Messages ----------------
def print_success(message):
    print(f"{SUCCESS} {message}")


def print_error(message):
    print(f"{ERROR} {message}")


def print_warning(message):
    print(f"{WARNING} {message}")


def print_info(message):
    print(f"{INFO} {message}")


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
        print(tabulate(data, headers="keys", tablefmt=tablefmt))
    else:
        print(tabulate(data, headers=headers, tablefmt=tablefmt))


# ---------------- Section Headers ----------------
def print_section(title, width=50):
    """
    Prints a section header with lines and centers the title.

    Args:
        title (str): The section title
        width (int): Total width of the section
    """
    print("\n" + "=" * width)
    print(Style.BRIGHT + title.center(width))
    print("=" * width)


# ---------------- Extra Info ----------------
def print_extra_info(info):
    """
    Prints extra info (like tries left or login status)
    """
    print(f"{INFO} {info}")
    print("-" * 50)
