import unittest
import os
import shutil
import json
from unittest.mock import patch

# Import models and controllers
from models.program_meta_model import ProgramMeta
from models.playlist_model import Playlist
from models.song_model import Song
from utils.file_manager import write_data, load_data
import settings

class TestPlaylistManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Run once before all tests."""
        # Use a test data file
        cls.test_data_folder = ".test_data"
        cls.test_data_file = os.path.join(cls.test_data_folder, "test_program_data.json")
        
        # Override settings to point to test file
        # Note: This requires file_manager to import DATA_FILE_PATH from settings, 
        # or we need to patch it. Since we modified file_manager to use settings, 
        # we can patch settings.DATA_FILE_PATH.
        
        if not os.path.exists(cls.test_data_folder):
            os.makedirs(cls.test_data_folder)

    def setUp(self):
        """Run before each test."""
        # Reset data file
        with open(self.test_data_file, "w") as f:
            json.dump({}, f)
            
        # Patch the DATA_PATH in file_manager
        self.patcher = patch('utils.file_manager.DATA_PATH', self.test_data_file)
        self.patcher.start()
        
        # Patch the DATA_FOLDER in file_manager
        self.patcher_folder = patch('utils.file_manager.DATA_FOLDER', self.test_data_folder)
        self.patcher_folder.start()

    def tearDown(self):
        """Run after each test."""
        self.patcher.stop()
        self.patcher_folder.stop()

    @classmethod
    def tearDownClass(cls):
        """Run once after all tests."""
        # Clean up test folder
        if os.path.exists(cls.test_data_folder):
            shutil.rmtree(cls.test_data_folder)

    # ----------------------------------------------------------------
    # 1. Test Models (CRUD)
    # ----------------------------------------------------------------
    
    def test_create_song(self):
        """Test creating a valid song."""
        song = Song("S-001", "Test Song", "Test Singer", "Test Genre")
        self.assertEqual(song.song_id, "S-001")
        self.assertEqual(song.song_name, "Test Song")

    def test_create_song_invalid(self):
        """Test validation for song creation."""
        with self.assertRaises(ValueError):
            Song("INVALID-ID", "Name", "Singer", "Genre")
        
        with self.assertRaises(ValueError):
            Song("S-001", "No", "Singer", "Genre") # Name too short

    def test_create_playlist(self):
        """Test creating a valid playlist."""
        pl = Playlist("Pl-001", "My Playlist", "Note", [])
        self.assertEqual(pl.playlist_id, "Pl-001")
        self.assertEqual(len(pl.added_songs), 0)

    def test_add_song_to_playlist(self):
        """Test adding a song to a playlist."""
        song = Song("S-001", "Song A", "Singer A", "Genre A")
        pl = Playlist("Pl-001", "My Playlist", "Note", [])
        pl.added_songs.append(song)
        
        self.assertEqual(len(pl.added_songs), 1)
        self.assertEqual(pl.added_songs[0].song_name, "Song A")

    def test_remove_song_from_playlist(self):
        """Test removing a song."""
        song = Song("S-001", "Song A", "Singer A", "Genre A")
        pl = Playlist("Pl-001", "My Playlist", "Note", [song])
        
        pl.added_songs.remove(song)
        self.assertEqual(len(pl.added_songs), 0)

    # ----------------------------------------------------------------
    # 2. Test Persistence (Save/Load)
    # ----------------------------------------------------------------

    def test_save_and_load_data(self):
        """Test saving program state and loading it back."""
        # Create state
        song = Song("S-001", "Saved Song", "Singer", "Genre")
        pl = Playlist("Pl-001", "Saved Playlist", "Note", [song])
        meta = ProgramMeta(latest_song_id=1, latest_playlist_id=1, playlists=[pl])
        
        # Save
        write_data(meta.to_dict())
        
        # Load
        loaded_data = load_data()
        loaded_meta = ProgramMeta.from_dict(loaded_data)
        
        self.assertEqual(loaded_meta.latest_song_id, 1)
        self.assertEqual(len(loaded_meta.playlists), 1)
        self.assertEqual(loaded_meta.playlists[0].playlist_name, "Saved Playlist")
        self.assertEqual(loaded_meta.playlists[0].added_songs[0].song_name, "Saved Song")

    # ----------------------------------------------------------------
    # 3. Test Export
    # ----------------------------------------------------------------
    
    def test_export_excel(self):
        """Test that export function creates a file."""
        from utils.export_utils import export_playlists_to_excel
        
        song = Song("S-001", "Export Song", "Singer", "Genre")
        pl = Playlist("Pl-001", "Export Playlist", "Note", [song])
        
        export_file = os.path.join(self.test_data_folder, "test_export.xlsx")
        
        # Run export
        export_playlists_to_excel([pl], export_file)
        
        # Check if file exists
        self.assertTrue(os.path.exists(export_file))

if __name__ == "__main__":
    unittest.main()
