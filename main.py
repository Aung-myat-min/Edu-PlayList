from controllers.welcome_controller import WelcomeController
from utils.menu_wrapper import run_menu
from views.welcome_view import WELCOME_MENU
from models.login_state import LoginState

def main():
    welcome_ctrl = WelcomeController()
    login_state = None
    tries_left = welcome_ctrl.login_ctrl.attempts_left

    while True:
        extra_info = None
        default_choice = None
        if login_state == LoginState.FAIL:
            extra_info = f" ❌ Login failed! Tries left: {tries_left}"
            default_choice = 1

        # Show welcome menu and get choice
        choice = run_menu(WELCOME_MENU, extra_info, default_choice)
        login_state = welcome_ctrl.handle_input(choice)

        # Handle login result
        if login_state == LoginState.SUCCESS:
            print("🎉 Login successful! You can continue...")
            break
        elif login_state == login_state.EXIT and tries_left > 1:
            print("Exiting program...")
            break
        elif login_state == LoginState.EXIT:
            print("⏹ Too many failed attempts. Exiting program...")
            break
        # If login fails but attempts remain, loop continues
        tries_left = welcome_ctrl.login_ctrl.attempts_left

if __name__ == "__main__":
    main()
