class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
    

happy_bday = Song([
    "Happy birthday to you",
    "I don't want to get sued",
    "so I'll stop right there"
])

bulls_on_parade = Song([
    "They rally around tha family",
    "With pockets full of shells"
])

my_daddy = Song([
    "My daddy my daddy",
    "Your baby is singing",
    "I will be sing and dancing and shouting",
    "for the rest of eternity!"
])

happy_bday.sing_me_a_song()

print('-' * 10)
bulls_on_parade.sing_me_a_song()

print('-' * 10)
my_daddy.sing_me_a_song()