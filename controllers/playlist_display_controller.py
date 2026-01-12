from tabulate import tabulate

from utils.console_utils import print_warning


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
