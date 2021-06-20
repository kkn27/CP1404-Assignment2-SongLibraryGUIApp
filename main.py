"""
Name: Kaung Khant Naing
Date: 24.5.2020
Brief Project Description:
GitHub URL:https://github.com/JCUS-CP1404/assignment-02-songs-app-kkn27
"""

# import modules that will be used in the program

from kivy.app import App
from kivy.lang import Builder
from songcollection import SongList
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput



FILE_NAME = 'songs'


class SongsToLearnApp(App):
    def build(self):
        self.title = "Songs to learn 2.0 by Kaung Khant Naing" # title for kivy spp
        self.root = Builder.load_file('app.kv') # opening kivy app with file name
        self.song_list.load_songs('songs.csv')
        self.root.ids.sort_options.values = self.song_list_options
        self.song_button_creator()
        return self.root

    def __init__(self):
        super().__init__()
        self.song_list = SongList()
        self.song_list.load_songs(FILE_NAME)
        self.song_list.sort_list("Artist")
        self.song_list_options = ['Artist', 'Title', 'Year', 'Learned']

    def song_button_creator(self):
        for item in self.song_list.songs:
            new_button = Button(text=str(item))
            self.root.ids.song_buttons.add_widget(new_button)

    def song_sorter(self):
        self.song_list.sort_list(self.root.ids.sort_options.text)
        self.root.ids.song_buttons.clear_widgets()
        self.song_button_creator()


    def handle_add_song(self):
        if self.root.ids.song_title.text == '' or \
                self.root.ids.song_artist.text == '' or \
                self.root.ids.song_year.text == '':
            self.root.ids.label_text_id.text = 'All fields must be completed'
        elif int(self.root.ids.song_year.text) < 0:
            self.root.ids.label_text_id.text = 'Year must be >= 0'
        elif not (self.root.ids.song_year.text.isdigit()):
            self.root.ids.label_text_id.text = 'Please enter a valid number'
        else:
            self.song_list.add_song(self.root.ids.song_title.text, self.root.ids.song_artist.text,
                                    self.root.ids.song_year.text, False)
            self.root.ids.label_text_id.text = self.root.ids.song_title.text + ' added'
            self.song_list.sort_list(self.root.ids.sort_options.text)
            self.root.ids.song_buttons.clear_widgets()
            self.song_button_creator()


def song_click_handler(self, button):
    """
        Handles on click for each song button created
    """

    # if button user clicked is learned change it to required to learn and update the status bar
    if self.song_list.get_song(button.id).status == 'n':
        self.song_list.get_song(button.id).status = 'y'
        self.root.ids.bottomLayout.text = "You need to learn " + str(self.song_list.get_song(button.id).title)

    # if button user clicked is Required to learn change it to learned and update the status bar
    else:
        self.song_list.get_song(button.id).status = 'n'
        self.root.ids.bottomLayout.text = "You have learned " + str(self.song_list.get_song(button.id).title)

    # Update the sorting and reloads the right layout
    self.sort_songs()
    self.root.ids.rightLayout.clear_widgets()
    self.build_right_widgets()


def clear_fields(self):
    self.root.ids.song_title.text = ''
    self.root.ids.song_artist.text = ''
    self.root.ids.song_year.text = ''
    self.root.ids.label_text_id.text = ''


def change_learned(self):
    pass


def __del__(self):
    self.song_list.save_songs(FILE_NAME)
    print(self.song_list)


SongsToLearnApp().run()