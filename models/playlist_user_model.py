class PlayListUser:
    """
    Represents a user in the playlist system.

    Each user has a unique user ID and a password. The class is responsible
    for validating input data during object creation and for verifying
    login credentials.

    Constraints:
    - user_id must be exactly 7 characters long
    - password must be at least 8 characters long
    """

    def __init__(self, user_id, password):
        """
        Initialize a PlayListUser instance.

        Args:
            user_id (str): Unique identifier for the user (exactly 7 characters).
            password (str): User password (minimum 8 characters).

        Raises:
            ValueError: If user_id or password does not meet length requirements.
        """
        if len(user_id) != 7:
            raise ValueError("user_id must be exactly 7 characters")

        if len(password) < 8:
            raise ValueError("password must be at least 8 characters")

        self._user_id = user_id
        self._password = password

    @property
    def user_id(self):
        """
        Return the user's ID.

        Returns:
            str: The user's unique identifier.
        """
        return self._user_id

    def match_password(self, user_id, password):
        """
        Verify that the provided credentials match this user.

        Args:
            user_id (str): User ID to verify.
            password (str): Password to verify.

        Returns:
            bool: True if both user_id and password match, otherwise False.
        """
        return user_id == self._user_id and password == self._password
