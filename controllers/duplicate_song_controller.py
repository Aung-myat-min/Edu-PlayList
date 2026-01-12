from collections import defaultdict
from utils.console_utils import print_info

def find_duplicate_songs(playlists):
    """
    Finds duplicate songs by name across playlists.
    """
    song_map = defaultdict(list)

    for p in playlists:
        for s in p.added_songs:
            song_map[s.song_name.lower()].append(p.playlist_name)

    duplicates = {
        name: pls for name, pls in song_map.items() if len(pls) > 1
    }

    if not duplicates:
        print_info("No duplicate songs found.")
        return

    for song, pls in duplicates.items():
        print(f"🎵 '{song}' appears in: {', '.join(pls)}")
