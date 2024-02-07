# getlyrics.py
This Python script uses the Genius API to fetch lyrics of all songs by a specified artist and saves them.

### Dependencies
```
os
lyricsgenius
re
sys
dotenv
```

### Environment Variables
GENIUS_TOKEN="xxx": This is your Genius API token. It is loaded from a .env file.


### Usage
```
python3 getlyrics.py Artist_name
```

---

# getstats.py

This Python script is used for reading lyrics and processing them.

### Dependencies
```
glob
collections
nltk
os
sys
```

### Parameters

`lyrics_language`: The language to use for tokenization.
`absolute_lyrics_file_path`: The file path pattern to use for reading files (using wildcards, and use quote)
`lyrics_num_common`: The number of most common words to return.

### Usage
To use this script run :
```
python3 getstats.py <lyrics_language> '<absolute_lyrics_file_path>' <lyrics_num_common>
``` 