import re


class Singer:
    """Represents a singer."""

    def __init__(self, singer_id, singer_name):
        """
        Create a Singer instance.

        Raises:
            ValueError: If validation fails.
        """
        if not re.fullmatch(r"Si-\d{3}", singer_id):
            raise ValueError("singer_id must follow the pattern Si-000")

        if len(singer_name) < 3:
            raise ValueError("singer_name must be at least 3 characters long")

        self.singer_id = singer_id
        self.singer_name = singer_name
