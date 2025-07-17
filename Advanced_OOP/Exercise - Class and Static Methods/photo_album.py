from math import ceil


class PhotoAlbum:
    PAGES_SIZE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: list[list[str]] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = photos_count / cls.PAGES_SIZE
        return cls(ceil(pages))

    def add_photo(self, label: str):
        for idx, page in enumerate(self.photos):
            if len(page) < 4:
                self.photos[idx].append(label)
                slot_index = len(self.photos[idx])
                return f"{label} photo added successfully on page {idx + 1} slot {slot_index}"
        return "No more free slots"

    def display(self):
        separator = "-" * 11
        result = [separator]

        for page in self.photos:
            result.append(" ".join("[]" for _ in range(len(page))))
            result.append(separator)

        return "\n".join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())


