import re

from settings import PLAYLIST_ID_PREFIX

class Playlist:
    """Represents a playlist."""

    def __init__(self, playlist_id, playlist_name, playlist_note, added_songs):
        """
        Create a Playlist instance.

        Raises:
            ValueError: If validation fails.
            TypeError: If added_songs is not a list of Song objects.
        """
        pattern = rf"^{PLAYLIST_ID_PREFIX}-\d{{3}}$"
        if not re.fullmatch(pattern, playlist_id):
            raise ValueError(f"playlist_id must follow the pattern {PLAYLIST_ID_PREFIX}-000")

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

    def __repr__(self):
        """Return a developer-friendly representation."""
        return (f"{self.__class__.__name__}(playlist_id='{self.playlist_id}', "
                f"playlist_name='{self.playlist_name}', playlist_note='{self.playlist_note}', "
                f"added_songs={self.added_songs})")

    def __str__(self):
        """Return a clean, labeled string for console output with songs in table format."""
        return "Dont' use normal print for this object. Instead use display method."

    def display(self):
        """Print playlist details in console with table."""
        from controllers.playlist_display_controller import display_playlist_songs
        
        print(f"PlaylistId: {self.playlist_id}")
        print(f"Name: {self.playlist_name}")
        print(f"Note: {self.playlist_note if self.playlist_note else 'None'}")
        print("Songs:")

        display_playlist_songs(self)

    # ---------------- Serialisation ----------------
    def to_dict(self):
        """Convert object to dictionary for JSON Serialisation."""
        return {
            "playlist_id": self.playlist_id,
            "playlist_name": self.playlist_name,
            "playlist_note": self.playlist_note,
            "added_songs": [song.to_dict() for song in self.added_songs]  # nested
        }

    @classmethod
    def from_dict(cls, data):
        from models.song_model import Song
        """Create a Playlist object from a dictionary."""
        songs = [Song.from_dict(s) for s in data.get("added_songs", [])]
        return cls(
            playlist_id=data["playlist_id"],
            playlist_name=data["playlist_name"],
            playlist_note=data.get("playlist_note"),
            added_songs=songs
        )