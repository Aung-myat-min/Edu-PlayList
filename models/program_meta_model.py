from settings import SONG_ID_PREFIX, PLAYLIST_ID_PREFIX


class ProgramMeta:
    """Manages global program state like latest IDs and playlists and Local caches."""

    def __init__(self, latest_song_id=0, latest_playlist_id=0, playlists=None):
        self.latest_song_id = latest_song_id
        self.latest_playlist_id = latest_playlist_id
        self.playlists = playlists if playlists else []

    # ---------- ID generation ----------
    def next_song_id(self):
        """Increment and return the next song ID as S-000 format."""
        self.latest_song_id += 1
        return f"{SONG_ID_PREFIX}-{self.latest_song_id:03d}"

    def next_playlist_id(self):
        """Increment and return the next playlist ID as Pl-000 format."""
        self.latest_playlist_id += 1
        return f"{PLAYLIST_ID_PREFIX}-{self.latest_playlist_id:03d}"

    # ---------- Playlist management ----------
    def add_playlist(self, playlist):
        """Add a playlist to the global list."""
        self.playlists.append(playlist)

    def get_playlist(self, playlist_id):
        """Retrieve a playlist by its ID. Returns None if not found."""
        for pl in self.playlists:
            if pl.playlist_id == playlist_id:
                return pl
        return None

    def list_playlists(self):
        """Return a copy of the playlists list."""
        return self.playlists.copy()

    def delete_playlist(self, playlist_id):
        """Remove a playlist by ID and return True if successful."""
        for i, pl in enumerate(self.playlists):
            if pl.playlist_id == playlist_id:
                del self.playlists[i]
                return True
        return False

    # ---------------- Serialisation ----------------
    def to_dict(self):
        """Convert entire program state to dictionary."""
        return {
            "latest_song_id": self.latest_song_id,
            "latest_playlist_id": self.latest_playlist_id,
            "playlists": [pl.to_dict() for pl in self.playlists]
        }

    @classmethod
    def from_dict(cls, data):
        from models.playlist_model import Playlist
        playlists = [Playlist.from_dict(pl) for pl in data.get("playlists", [])]
        return cls(
            latest_song_id=data.get("latest_song_id", 0),
            latest_playlist_id=data.get("latest_playlist_id", 0),
            playlists=playlists
        )