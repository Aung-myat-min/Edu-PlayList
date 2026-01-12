SONG_ID_PREFIX = "S"
PLAYLIST_ID_PREFIX = "Pl"
DATA_FILE_PATH = ".data/program_data.json"
LOCKED_OUT_TIME_SECONDS = 300  # 5 minutes

from models.playlist_user_model import PlayListUser

# PROGRAM_MAIN_STATE = ProgramMeta()
PROGRAM_USER = PlayListUser("user123", "Givemetheykey123")