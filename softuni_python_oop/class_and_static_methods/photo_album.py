import math


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(math.ceil(photos_count / 4))

    def add_photo(self, label: str):
        for i, photo in enumerate(self.photos):
            if len(photo) < 4:
                photo.append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(photo)}"
        return "No more free slots"

    def display(self):
        separator = "-" * 11 + "\n"
        result = separator
        for photos in self.photos:
            result += " ".join(["[]"for _ in photos]) + "\n"
            result += separator
        return result.strip()


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())


