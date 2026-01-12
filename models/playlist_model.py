import re


class Playlist:
    """Represents a playlist."""

    def __init__(self, playlist_id, playlist_name, playlist_note, added_songs):
        """
        Create a Playlist instance.

        Raises:
            ValueError: If validation fails.
            TypeError: If added_songs is not a list of Song objects.
        """
        if not re.fullmatch(r"Pl-\d{3}", playlist_id):
            raise ValueError("playlist_id must follow the pattern Pl-000")

        if len(playlist_name) < 3:
            raise ValueError("playlist_name must be at least 3 characters long")

        if playlist_note is not None and len(playlist_note) < 3:
            raise ValueError("playlist_note must be at least 3 characters long")

        if not isinstance(added_songs, list):
            raise TypeError("added_songs must be a list")

        # Validate list contains Song objects
        for song in added_songs:
            if song.__class__.__name__ != "Song":
                raise TypeError("added_songs must contain only Song objects")

        self.playlist_id = playlist_id
        self.playlist_name = playlist_name
        self.playlist_note = playlist_note
        self.added_songs = added_songs
