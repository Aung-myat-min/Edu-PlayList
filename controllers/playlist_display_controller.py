from tabulate import tabulate

from utils.console_utils import print_warning, print_table


def _shorten(text, max_len=10):
    return text if len(text) <= max_len else text[:max_len] + "..."

def display_playlist_overview(playlists):
    """
    Displays playlists in a minimal overview table.
    """
    if not playlists:
        print_warning("No playlists available.")
        return

    table = []
    for p in playlists:
        table.append([
            p.playlist_id,
            _shorten(p.playlist_name),
            _shorten(p.playlist_note or "None"),
            len(p.added_songs)
        ])

    print(tabulate(
        table,
        headers=["ID", "Name", "Note", "#Songs"],
        tablefmt="fancy_grid"
    ))

def display_playlist_songs(playlist):
    """
    Displays songs in a playlist in a table format.
    """
    if not playlist.added_songs:
        print_warning("No songs in this playlist.")
        return

    table_data = [song.to_dict() for song in playlist.added_songs]
    print_table(table_data, headers=["ID", "Name", "Singer", "Genre"])