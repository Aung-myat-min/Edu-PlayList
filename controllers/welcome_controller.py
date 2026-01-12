from models.login_state import LoginState
from controllers.login_controller import LoginController
from utils.input_controller import get_valid_input
from utils.console_utils import print_warning


class WelcomeController:
    def __init__(self):
        self.login_ctrl = LoginController()

    def handle_input(self, choice):
        """
        Handle user's selection from welcome menu.

        Returns:
            LoginState
        """
        if choice == 1:
            # Check if locked out before asking for input to save user time
            if self.login_ctrl.is_locked_out():
                return LoginState.LOCKED

            username = get_valid_input("Enter username: ", 1)
            password = get_valid_input("Enter password: ", 1)
            return self.login_ctrl.verify_login(username, password)
        elif choice == 0:
            return LoginState.EXIT
        else:
            print("❌ Invalid option.")
            return None