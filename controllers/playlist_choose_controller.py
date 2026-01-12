from utils.console_utils import print_success, print_warning, print_info
from controllers.playlist_display_controller import display_playlist_overview


def choose_playlist(playlists):
    """
    Prompt user to choose a playlist by ID.
    Keeps prompting until a valid ID is entered or user exits with 'e'.

    Returns:
        str | None: playlist_id if selected, None if exited
    """
    if not playlists:
        print_warning("No playlists available.")
        return None

    while True:
        display_playlist_overview(playlists)
        print_info("Enter playlist ID to select, or 'e' to exit")

        user_input = input("Playlist ID (or e): ").strip()

        # Exit condition
        if user_input.lower() == "e":
            print_info("Exited playlist selection.")
            return None

        # Validate input length (reuse your rule)
        if len(user_input) < 3:
            print_warning("Input must be at least 3 characters.")
            continue

        # Check existence
        for p in playlists:
            if p.playlist_id == user_input:
                print_success(f"Playlist '{p.playlist_name}' selected.")
                return p.playlist_id

        print_warning("Playlist not found. Try again.")
