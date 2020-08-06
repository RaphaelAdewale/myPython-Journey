class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "with pockets full of shells"])

words = """I just want to be here you are,
sitting in your presence always"""

don_moen = Song([words])

don_moen.sing_me_a_song()

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
