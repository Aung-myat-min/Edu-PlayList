from utils.menu_wrapper import run_menu
from views.playlist_inner_menu_view import PLAYLIST_INNER_MENU
from controllers.playlist_inner_controller import (
    show_playlist_details,
    add_song_to_playlist,
    edit_song_in_playlist,
    delete_song_from_playlist,
    shuffle_playlist_songs,
    sort_playlist_songs_asc
)

def playlist_inner_loop(playlist, program_state):
    """
    Handles the playlist inner menu (song-level actions)
    """

    while True:
        choice = run_menu(PLAYLIST_INNER_MENU)

        match choice:
            case 1:
                show_playlist_details(playlist)

            case 2:
                add_song_to_playlist(playlist, program_state.next_song_id())

            case 3:
                edit_song_in_playlist(playlist)

            case 4:
                delete_song_from_playlist(playlist)

            case 5:
                shuffle_playlist_songs(playlist)

            case 6:
                sort_playlist_songs_asc(playlist)

            case 0:
                print("⬅️ Returning to Playlist Menu...")
                break
