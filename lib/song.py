class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the song count
        Song.add_song_to_count()

        # Add genre and artist
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

        # Update genre and artist counts
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def get_genres(cls):
        return cls.genres

    @classmethod
    def get_artists(cls):
        return cls.artists

    @classmethod
    def get_genre_count(cls):
        return cls.genre_count

    @classmethod
    def get_artist_count(cls):
        return cls.artist_count

# Example usage:
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
hello = Song("Hello", "Adele", "Pop")
formation = Song("Formation", "Beyonce", "Pop")

print(Song.get_count())  # Output: 3
print(Song.get_genres())  # Output: ["Rap", "Pop"]
print(Song.get_artists())  # Output: ["Jay-Z", "Adele", "Beyonce"]
print(Song.get_genre_count())  # Output: {"Rap": 1, "Pop": 2}
print(Song.get_artist_count())  # Output: {"Jay-Z": 1, "Adele": 1, "Beyonce": 1}
