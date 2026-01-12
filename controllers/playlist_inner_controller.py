import random

from utils.console_utils import print_success, print_warning
from controllers.song_choose_controller import choose_song
from controllers.playlist_display_controller import display_playlist_songs
from models.song_model import Song
from settings import SONG_ID_PREFIX
from utils.input_controller import get_valid_input


def show_playlist_details(playlist):
    playlist.display()


def add_song_to_playlist(playlist, next_song_id):

    song_name = get_valid_input("Song name: ")
    singer_name = get_valid_input("Singer name: ")
    genre_name = get_valid_input("Genre name: ")

    try:
        song = Song(next_song_id, song_name, singer_name, genre_name)
        playlist.added_songs.append(song)
        print_success(f"Song '{song_name}' added.")
        display_playlist_songs(playlist)
    except ValueError as e:
        print_warning(str(e))


def edit_song_in_playlist(playlist):
    song = choose_song(playlist.added_songs)
    if not song:
        return

    song.song_name = get_valid_input("New song name: ", default=song.song_name)
    song.singer_name = get_valid_input("New singer name: ", default=song.singer_name)
    song.genre_name = get_valid_input("New genre name: ", default=song.genre_name)

    print_success("Song updated successfully.")
    display_playlist_songs(playlist)


def delete_song_from_playlist(playlist):
    song = choose_song(playlist.added_songs)
    if not song:
        return

    playlist.added_songs.remove(song)
    print_success(f"Song '{song.song_name}' deleted.")
    display_playlist_songs(playlist)


def shuffle_playlist_songs(playlist):
    if len(playlist.added_songs) < 2:
        print_warning("Not enough songs to shuffle.")
        return

    random.shuffle(playlist.added_songs)
    print_success("Playlist shuffled.")
    display_playlist_songs(playlist)

def sort_playlist_songs_asc(playlist):
    if len(playlist.added_songs) < 2:
        print_warning("Not enough songs to sort.")
        return

    playlist.added_songs.sort(key=lambda s: s.song_name.lower())
    print_success("Songs sorted A → Z.")
    display_playlist_songs(playlist)

def edit_playlist_name(playlist):
    new_name = get_valid_input("Enter new playlist name: ", default=playlist.playlist_name)
    playlist.playlist_name = new_name
    print_success(f"Playlist renamed to '{new_name}'.")