from controllers.playlist_controller import list_playlists, create_playlist, delete_playlist, sort_playlists_asc, \
    sort_playlists_desc, show_duplicates, export_playlists, choose_a_playlist
from controllers.welcome_controller import WelcomeController
from models.program_meta_model import ProgramMeta
from playlist_inner_menu import playlist_inner_loop
from utils.console_utils import print_error, print_warning
from utils.menu_wrapper import run_menu
from views.playlist_menu_view import PLAYLIST_MENU
from views.welcome_view import WELCOME_MENU
from models.login_state import LoginState
from utils.file_manager import load_data, write_data

def load_program_state():
    try:
        raw = load_data()

        # If file is empty or doesn't exist
        if not raw:
            return ProgramMeta(0, 0, [])

        return ProgramMeta.from_dict(raw)
    except (ValueError, TypeError, KeyError) as e:
        # This catches validation errors from your models (like Pl-000 format issues)
        print_error(f"Failed to load saved data: {e}")
        print_warning("Starting with a fresh program state to prevent crash.")
        return ProgramMeta(0, 0, [])
    except Exception as e:
        # General catch-all for unexpected file system or JSON issues
        print_error(f"An unexpected error occurred while loading data: {e}")
        return ProgramMeta(0, 0, [])

def save_program_state(program_state):
    write_data(program_state.to_dict())

def main():
    welcome_ctrl = WelcomeController()
    login_state = None
    tries_left = welcome_ctrl.login_ctrl.attempts_left

    # -------- Login Loop --------
    while True:
        extra_info = None
        default_choice = None

        if login_state == LoginState.FAIL:
            extra_info = f" ❌ Login failed! Tries left: {tries_left}"
            default_choice = 1

        choice = run_menu(WELCOME_MENU, extra_info, default_choice)
        login_state = welcome_ctrl.handle_input(choice)

        if login_state == LoginState.SUCCESS:
            print("🎉 Login successful!\n")
            break

        elif login_state == LoginState.EXIT:
            print("👋 Exiting program...")
            return

        tries_left = welcome_ctrl.login_ctrl.attempts_left

    # -------- Load Program State --------
    program_state = load_program_state()
    playlists = program_state.playlists

    # -------- Playlist Menu --------
    while True:
        choice = run_menu(PLAYLIST_MENU)

        match choice:
            case 1:
                list_playlists(playlists)

            case 2:
                chosen_playlist_id = choose_a_playlist(playlists)
                if chosen_playlist_id:
                    chosen_playlist = program_state.get_playlist(chosen_playlist_id)
                    if chosen_playlist:
                        playlist_inner_loop(chosen_playlist, program_state)
                        save_program_state(program_state)
                    else:
                        print_error("Playlist not found!")

            case 3:
                try:
                    # Use a temporary ID to not increment the state if creation fails
                    next_id = program_state.next_playlist_id()
                    create_playlist(playlists, next_id)
                    save_program_state(program_state)
                except ValueError as e:
                    program_state.latest_playlist_id -= 1
                    print_error(f"Could not create playlist: {e}")

            case 4:
                delete_playlist(playlists)
                save_program_state(program_state)

            case 5:
                sort_playlists_asc(playlists)

            case 6:
                sort_playlists_desc(playlists)

            case 7:
                show_duplicates(playlists)

            case 8:
                export_playlists(playlists)

            case 0:
                save_program_state(program_state)
                print("👋 Logged out.")
                break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️ Program interrupted. Saving state and exiting...")
    except Exception as e:
        print(f"❌ Critical Error: {e}")
