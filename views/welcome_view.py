from utils.menu_wrapper import run_menu

WELCOME_MENU = {
    "title": "🎵 Welcome to My Playlist App 🎵",
    "options": [
        {"key": 1, "label": "Login", "action": "login"},
        {"key": 0, "label": "Exit", "action": "exit"}
    ]
}


def display_welcome_menu(tries_left, login_state):
    """
    Display the welcome menu with tries left and login status.

    Args:
        tries_left (int): Number of login attempts left.
        login_state (LoginState): Current state of login.
    """
    print("\n" + "=" * 40)
    print(WELCOME_MENU["title"])
    print("=" * 40)

    # Login state feedback
    if login_state == "FAIL":
        print(f"❌ Login failed! Tries left: {tries_left}")
    elif login_state == "SUCCESS":
        print("✅ Login successful!")

    # Display menu options
    run_menu(WELCOME_MENU)
