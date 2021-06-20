"""
(incomplete) Tests for SongList class
"""
from songcollection import SongList
from song import Song
from operator import attrgetter

# test empty SongList
song_collection = SongList()
assert len(song_collection.songs) == 0

# test loading songs
song_collection.load_songs('songs.csv')
assert len(song_collection.songs) > 0  # assuming CSV file is not empty
print(song_collection)


# test get number of songs to learn
print("Number of songs to learn = ", song_collection.get_number_required())


# test sorting songs
#song_list.sort_list(song_list.songs[0].title)
song_collection.sort_list("Required")
print('\n\n', song_collection)


# test adding a new Song
song_collection.add_song("Here and Now","Someone",1981,False)
print(song_collection)


# test getting the number of required and learned songs (separately)
print("Number of songs learnt = ", song_collection.get_number_learned())
# test saving songs (check CSV file manually to see results)
song_collection.save_songs("songs.csv")
