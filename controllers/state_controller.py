from models.program_meta_model import ProgramMeta
from utils.file_manager import load_data, write_data
from utils.console_utils import print_error, print_warning

def load_program_state():
    """Loads the program state from storage."""
    try:
        raw = load_data()
        if not raw:
            return ProgramMeta(0, 0, [])
        return ProgramMeta.from_dict(raw)
    except (ValueError, TypeError, KeyError) as e:
        print_error(f"Failed to load saved data: {e}")
        print_warning("Starting with a fresh program state to prevent crash.")
        return ProgramMeta(0, 0, [])
    except Exception as e:
        print_error(f"An unexpected error occurred while loading data: {e}")
        return ProgramMeta(0, 0, [])

def save_program_state(program_state):
    """Saves the current program state to storage."""
    write_data(program_state.to_dict())
