from enum import Enum

class LoginState(Enum):
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"
    EXIT = "EXIT"
    LOCKED = "LOCKED"