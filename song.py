"""
Name: Kaung Khant Naing
Date Started: 24.5.2020
GitHUb URL: https://github.com/JCUS-CP1404/assignment-02-songs-app-kkn27
"""

class Song:
    def __init__(self, title='', artist='', year=0, is_learned='y'):
        self.artist = artist.title()
        self.title = title.title()
        self.year = int(year)
        if is_learned.lower() == 'y':
            self.is_learned = False
        elif is_learned.lower() == 'n':
            self.is_learned = True
        else:
            self.is_learned = is_learned

    def set_learnt(self):
        self.is_learned = True

    def set_not_learnt(self):
        self.is_learned = False

    def __str__(self):
        return "\'{}\' by {} ({:4}) {}".format(self.title, self.artist, self.year, (('(learned)', '')[self.is_learned==False]))
