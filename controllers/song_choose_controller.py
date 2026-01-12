from utils.console_utils import print_warning, print_success, print_info
from tabulate import tabulate

from utils.input_controller import get_valid_input


def choose_song(songs):
    """
    Let user choose a song by ID.
    User can enter 'e' to exit.

    Returns:
        Song | None
    """
    if not songs:
        print_warning("No songs in this playlist.")
        return None

    while True:
        # Display song list (minimal)
        table_data = [
            [s.song_id, s.song_name, s.singer_name, s.genre_name]
            for s in songs
        ]

        print(tabulate(
            table_data,
            headers=["ID", "Name", "Singer", "Genre"],
            tablefmt="fancy_grid"
        ))

        print_info("Enter song ID to select, or 'e' to exit")
        user_input = get_valid_input("Song ID (or e): ", 1)

        if user_input.lower() == "e":
            print_info("Exited song selection.")
            return None

        for song in songs:
            if song.song_id == user_input:
                print_success(f"Song '{song.song_name}' selected.")
                return song

        print_warning("Song not found. Try again.")
