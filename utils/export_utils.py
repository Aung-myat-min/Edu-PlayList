from openpyxl import Workbook
from utils.console_utils import print_success, print_warning


def export_playlists_to_excel(playlists, file_name):
    """
    Export all playlists to an Excel file.

    Each playlist will have:
      - Playlist Name as a header
      - Table of songs: ID, Name, Singer, Genre

    Args:
        playlists (list): List of Playlist objects
        file_name (str): Name of the Excel file to create
    """
    if not playlists:
        print_warning("No playlists to export.")
        return

    wb = Workbook()
    wb.remove(wb.active)  # remove default sheet

    for playlist in playlists:
        # Sheet name: Playlist name (max 31 chars for Excel)
        sheet_name = playlist.playlist_name[:31]
        ws = wb.create_sheet(title=sheet_name)

        # Header
        ws.append(["Playlist Name:", playlist.playlist_name])
        ws.append(["Playlist Note:", playlist.playlist_note or ""])
        ws.append([])
        ws.append(["Song ID", "Name", "Singer", "Genre"])

        # Add songs
        for song in playlist.added_songs:
            ws.append([song.song_id, song.song_name, song.singer_name, song.genre_name])

        # Optional: auto-adjust column widths
        for col in ws.columns:
            max_length = 0
            column = col[0].column_letter
            for cell in col:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            ws.column_dimensions[column].width = max_length + 2

    # Save the workbook
    try:
        wb.save(file_name)
        print_success(f"✅ Playlists exported successfully to '{file_name}'")
    except Exception as e:
        print_warning(f"Failed to export playlists: {e}")
