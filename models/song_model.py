import re


class Song:
    """Represents a song."""

    def __init__(self, song_id, song_name, singer_id, genre_id):
        """
        Create a Song instance.

        Raises:
            ValueError: If validation fails.
        """
        if not re.fullmatch(r"S-\d{3}", song_id):
            raise ValueError("song_id must follow the pattern S-000")

        if len(song_name) < 3:
            raise ValueError("song_name must be at least 3 characters long")

        if not re.fullmatch(r"Si-\d{3}", singer_id):
            raise ValueError("singer_id must follow the pattern Si-000")

        if not re.fullmatch(r"G-\d{3}", genre_id):
            raise ValueError("genre_id must follow the pattern G-000")

        # TODO: Validate singer_id existence (e.g., check against Singer storage)
        # TODO: Validate genre_id existence (e.g., check against Genre storage)

        self.song_id = song_id
        self.song_name = song_name
        self.singer_id = singer_id
        self.genre_id = genre_id
