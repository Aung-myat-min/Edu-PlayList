import time
import sys
from controllers.welcome_controller import WelcomeController
from models.login_state import LoginState
from utils.menu_wrapper import run_menu
from views.welcome_view import WELCOME_MENU
from utils.console_utils import print_error
from controllers.playlist_controller import (
    list_playlists, create_playlist, delete_playlist, 
    sort_playlists_asc, sort_playlists_desc, show_duplicates, 
    export_playlists, choose_a_playlist
)
from playlist_inner_menu import playlist_inner_loop
from views.playlist_menu_view import PLAYLIST_MENU
from controllers.state_controller import save_program_state

# ==========================================
# Login Flow
# ==========================================

def _handle_lockout(login_ctrl):
    """Handles the UI for the lockout state."""
    print_error("🔒 System locked due to too many failed attempts.")
    try:
        while login_ctrl.is_locked_out():
            remaining = login_ctrl.get_remaining_lockout_time()
            mins, secs = divmod(remaining, 60)
            print(f"\r⏳ Please wait {mins:02d}:{secs:02d} before trying again...", end="", flush=True)
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\n👋 Exiting program...")
        sys.exit(0)
    
    # Clear line and notify
    print("\r" + " " * 60 + "\r", end="")
    print("✅ System unlocked. You may try again.\n")

def run_login_flow():
    """
    Runs the login loop.
    Returns:
        bool: True if login successful, False if user wants to exit.
    """
    welcome_ctrl = WelcomeController()
    login_state = None
    
    while True:
        # 1. Handle Lockout
        if welcome_ctrl.login_ctrl.is_locked_out():
            _handle_lockout(welcome_ctrl.login_ctrl)
            login_state = None # Reset state after lockout

        # 2. Prepare Menu Info
        extra_info = None
        default_choice = None
        tries_left = welcome_ctrl.login_ctrl.attempts_left

        if login_state == LoginState.FAIL:
            extra_info = f" ❌ Login failed! Tries left: {tries_left}"
            default_choice = 1
        
        # 3. Show Menu & Get Input
        choice = run_menu(WELCOME_MENU, extra_info, default_choice)
        login_state = welcome_ctrl.handle_input(choice)

        # 4. Handle Result
        if login_state == LoginState.SUCCESS:
            print("🎉 Login successful!\n")
            return True

        elif login_state == LoginState.EXIT:
            print("👋 Exiting program...")
            return False

# ==========================================
# Main Application Flow
# ==========================================

def run_app_loop(program_state):
    """Runs the main application menu loop."""
    playlists = program_state.playlists

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
