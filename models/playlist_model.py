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

    def __repr__(self):
        """Return a developer-friendly representation."""
        return (f"{self.__class__.__name__}(playlist_id='{self.playlist_id}', "
                f"playlist_name='{self.playlist_name}', playlist_note='{self.playlist_note}', "
                f"added_songs={self.added_songs})")

    def __str__(self):
        """Return a clean, labeled string for console output with songs in table format."""
        note_str = self.playlist_note if self.playlist_note else "None"

        if not self.added_songs:
            songs_table = "No songs"
        else:
            # Prepare table header
            songs_table = f"{'ID':<8} {'Name':<25} {'Singer':<20} {'Genre':<15}\n"
            songs_table += "-" * 70 + "\n"

            # Add each song
            for song in self.added_songs:
                songs_table += f"{song.song_id:<8} {song.song_name:<25} {song.singer_name:<20} {song.genre_name:<15}\n"

        return (f"PlaylistId: {self.playlist_id}\n"
                f"Name: {self.playlist_name}\n"
                f"Note: {note_str}\n"
                f"Songs:\n{songs_table}")
