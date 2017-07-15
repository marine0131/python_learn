import time
class Song:
    def __init__(self, name):
        self.name=name

    def set_lyrics(self, lyrics):
        self.lyrics = lyrics
    def set_singer(self, singer):
        slef.singer = singer
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            time.sleep(0.1)
    
happy = Song('happy')
lyrics_file=open('ex40_song.txt')
lyrics=[]
for line in lyrics_file:
    lyrics.append(line)
happy.set_lyrics(lyrics)

happy.sing_me_a_song()
