import re

class Genre:
    """Represents a music genre."""

    def __init__(self, genre_id, genre_name):
        """
        Create a Genre instance.

        Raises:
            ValueError: If validation fails.
        """
        if not re.fullmatch(r"G-\d{3}", genre_id):
            raise ValueError("genre_id must follow the pattern G-000")

        if len(genre_name) < 3:
            raise ValueError("genre_name must be at least 3 characters long")

        self.genre_id = genre_id
        self.genre_name = genre_name

    def __repr__(self):
        """Return a developer-friendly representation."""
        return f"{self.__class__.__name__}(genre_id='{self.genre_id}', genre_name='{self.genre_name}')"

    def __str__(self):
        """Return a clean, labeled string for console output."""
        return f"GenreId: {self.genre_id},\nName: {self.genre_name}"
