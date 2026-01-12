import time
from models.login_state import LoginState
from settings import PROGRAM_USER, LOCKED_OUT_TIME_SECONDS

MAX_ATTEMPTS = 3

class LoginController:
    def __init__(self):
        self.attempts_left = MAX_ATTEMPTS
        self.lockout_end_time = 0

    def verify_login(self, input_username, input_password):
        """
        Verify user credentials.

        Returns:
            LoginState: SUCCESS if correct, FAIL if incorrect, LOCKED if locked out, EXIT if user chooses to exit.
        """
        # Check if currently locked out
        if self.is_locked_out():
            return LoginState.LOCKED

        if PROGRAM_USER.match_password(input_username, input_password):
            self.attempts_left = MAX_ATTEMPTS  # Reset attempts on success
            return LoginState.SUCCESS
        else:
            self.attempts_left -= 1
            if self.attempts_left <= 0:
                self.lockout_end_time = time.time() + LOCKED_OUT_TIME_SECONDS
                self.attempts_left = MAX_ATTEMPTS # Reset attempts for after lockout
                return LoginState.LOCKED
            return LoginState.FAIL

    def is_locked_out(self):
        """Check if the user is currently locked out."""
        if time.time() < self.lockout_end_time:
            return True
        return False

    def get_remaining_lockout_time(self):
        """Return remaining lockout time in seconds."""
        remaining = self.lockout_end_time - time.time()
        return max(0, int(remaining))