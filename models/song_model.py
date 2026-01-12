import re

class Song:
    """Represents a song."""

    def __init__(self, song_id, song_name, singer_name, genre_name):
        """
        Create a Song instance.

        Raises:
            ValueError: If validation fails.
        """
        if not re.fullmatch(r"S-\d{3}", song_id):
            raise ValueError("song_id must follow the pattern S-000")

        if len(song_name) < 3:
            raise ValueError("song_name must be at least 3 characters long")

        if len(singer_name) < 3:
            raise ValueError("singer_name must be at least 3 characters long")

        if len(genre_name) < 3:
            raise ValueError("genre_name must be at least 3 characters long")

        self.song_id = song_id
        self.song_name = song_name
        self.singer_name = singer_name
        self.genre_name = genre_name

    def __repr__(self):
        """Return a developer-friendly representation."""
        return (f"{self.__class__.__name__}(song_id='{self.song_id}', "
                f"song_name='{self.song_name}', singer_name='{self.singer_name}', "
                f"genre_name='{self.genre_name}')")

    def __str__(self):
        """Return a clean, labeled string for console output."""
        return (f"SongId: {self.song_id},\nName: {self.song_name},\n"
                f"Singer: {self.singer_name},\nGenre: {self.genre_name}")
