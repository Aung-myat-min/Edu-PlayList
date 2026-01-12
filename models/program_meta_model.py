from settings import SONG_ID_PREFIX, PLAYLIST_ID_PREFIX


class ProgramMeta:
    """Manages global program state like latest IDs and playlists and Local caches."""

    latest_song_id = 0
    latest_playlist_id = 0
    playlists = []

    def __init__(self, latest_song_id=0, latest_playlist_id=0, playlists=None):
        self.latest_song_id = latest_song_id
        self.latest_playlist_id = latest_playlist_id
        self.playlists = playlists if playlists is not None else []

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
