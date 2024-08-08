"""
Creational design patterns are related to the creation of objects, and Factory Method is a design pattern that
creates objects with a common interface.

https://realpython.com/factory-method-python/
"""
import json


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    def _get_serializer(self, song_format):
        """
        separate component with the responsibility to decide which concrete implementation should be used
        method does not call the concrete implementation, and it just returns the function object itself.
        called a creator component
        """
        if song_format == "JSON":
            return self._serialize_to_json
        else:
            raise ValueError("Unknown format")

    def _serialize_to_json(self, song):
        song_info = {
            "song_id": song.song_id,
            "title": song.title,
            "artist": song.artist
        }
        return json.dumps(song_info)

    def serialize(self, song, song_format):
        """one method which implementation does not change
            this method is the application code that depends on an interface to complete its task
            called a client component
        """
        serializer = self._get_serializer(song_format)
        return serializer(song)

def test_factory():
    song_serializer = SongSerializer()
    song = Song(1, "Pull Me Under", "DT")
    print(song_serializer.serialize(song, "JSON"))


if __name__ == "__main__":
    test_factory()
