class Book:
    def __init__(self, title, author):
        self.title = title
        self.athor = author

    def __str__(self):
        return f"{self.title} written by {self.author}"

