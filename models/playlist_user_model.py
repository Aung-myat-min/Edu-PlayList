class PlayListUser:
    def __init__(self, user_id, password):
        self._user_id = user_id
        self._password = password

    @property
    def user_id(self):
        return self._user_id

    def match_password(self, user_id, password):
        return user_id == self._user_id and password == self._password
