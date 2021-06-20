"""(Incomplete) Tests for Song class."""
from song import Song

# test empty song (defaults)
song = Song()
songlist = []
print(song)
assert song.artist == ""
assert song.title == ""
assert song.year == 0
assert song.is_learned==""

# test initial-value song
song2 = Song("Amazing Grace", "John Newton", 1779, True)
songlist.append(song2)
song2 = Song("I want to hold your hand)", "The beatles", 1962, False)
songlist.append(song2)
song2 = Song("its now or never)", "Unknow Artist", 1956, True)
songlist.append(song2)
for item in songlist:
    print(item)
