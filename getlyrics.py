import os
import lyricsgenius
import re
import sys
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GENIUS_TOKEN")

genius = lyricsgenius.Genius(token, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

def sanitize_filename(filename):
    """
    Sanitize the filename to remove characters that might not be supported by the filesystem.
    """
    return re.sub(r'[\\/*?:"<>|]', "", filename)

def get_all_songs_and_save_lyrics(artist_name):
    """
    Retrieves all songs by the specified artist from the Genius API and saves the lyrics to individual text files.
    """
    artist = genius.search_artist(artist_name, max_songs=None, sort='title')
    if artist:
        print(f"Found artist: {artist.name} with {len(artist.songs)} songs.")
        for song in artist.songs:
            filename = f"{sanitize_filename(song.title)}.txt"
            folder_name = sanitize_filename(artist_name)
            os.makedirs(folder_name, exist_ok=True)
            file_path = os.path.join(folder_name, filename)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(song.lyrics)
            print(f"Lyrics for '{song.title}' saved to {file_path}.")
    else:
        print("Artist not found.")

if len(sys.argv) < 2:
    print("Please provide an artist name as a command-line argument.")
else:
    artist_name = sys.argv[1]
    get_all_songs_and_save_lyrics(artist_name)

