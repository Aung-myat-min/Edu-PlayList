from models.login_state import LoginState
from settings import PROGRAM_USER

MAX_ATTEMPTS = 3

class LoginController:
    def __init__(self):
        self.attempts_left = MAX_ATTEMPTS

    def verify_login(self, input_username, input_password):
        """
        Verify user credentials.

        Returns:
            LoginState: SUCCESS if correct, FAIL if incorrect, EXIT if no attempts left.
        """
        if PROGRAM_USER.match_password(input_username, input_password):
            return LoginState.SUCCESS
        else:
            self.attempts_left -= 1
            if self.attempts_left <= 0:
                return LoginState.EXIT
            return LoginState.FAIL
