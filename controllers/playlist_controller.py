from controllers.playlist_display_controller import display_playlist_overview
from controllers.playlist_choose_controller import choose_playlist
from controllers.duplicate_song_controller import find_duplicate_songs
from utils.input_controller import get_valid_input
from utils.console_utils import print_success, print_info
from models.playlist_model import Playlist
from settings import PLAYLIST_ID_PREFIX

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
    playlist = choose_playlist(playlists)
    if playlist:
        playlists.remove(playlist)
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
    # TODO: implement actual export
    print_success("Playlists exported successfully.")

def show_duplicates(playlists):
    find_duplicate_songs(playlists)
