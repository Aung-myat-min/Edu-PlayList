from controllers.playlist_display_controller import display_playlist_overview
from controllers.playlist_choose_controller import choose_playlist
from controllers.duplicate_song_controller import find_duplicate_songs
from utils.export_utils import export_playlists_to_excel
from utils.input_controller import get_valid_input
from utils.console_utils import print_success, print_info
from models.playlist_model import Playlist
from utils.string_utils import clean_input


def list_playlists(playlists):
    display_playlist_overview(playlists)

def create_playlist(playlists, next_id):
    name = get_valid_input("Playlist name: ")
    note = get_valid_input("Playlist note: ")
    print(next_id)
    playlist = Playlist(
        playlist_id=next_id,
        playlist_name=name,
        playlist_note=note,
        added_songs=[]
    )

    playlists.append(playlist)
    print_success("Playlist created successfully.")

def choose_a_playlist(playlists):
    playlist = choose_playlist(playlists)
    return playlist

def delete_playlist(playlists):
    playlist_id = choose_playlist(playlists)
    if playlist_id:
        playlists.delete_playlist(playlist_id)
        print_success("Playlist deleted.")

def sort_playlists_asc(playlists):
    playlists.sort(key=lambda p: p.playlist_name.lower())
    print_info("Playlists sorted A → Z.")
    display_playlist_overview(playlists)

def sort_playlists_desc(playlists):
    playlists.sort(key=lambda p: p.playlist_name.lower(), reverse=True)
    print_info("Playlists sorted Z → A.")
    display_playlist_overview(playlists)

def export_playlists(playlists):
    """
    Ask the user for a file name and export playlists.
    Currently, just prints a success message (actual export TBD).
    """
    file_name = clean_input(input("Enter export file name (default: your_playlists.xlsx): ").strip())

    if not file_name:
        file_name = "your_playlists.xlsx"
    elif not file_name.endswith(".xlsx"):
        file_name += ".xlsx"

    export_playlists_to_excel(playlists, file_name)

    print_success(f"Playlists exported successfully to '{file_name}'")

def show_duplicates(playlists):
    find_duplicate_songs(playlists)
