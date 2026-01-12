from models.login_state import LoginState
from controllers.login_controller import LoginController


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
            username = input("Enter username: ")
            password = input("Enter password: ")
            return self.login_ctrl.verify_login(username, password)
        elif choice == 0:
            return LoginState.EXIT
        else:
            print("❌ Invalid option.")
            return None