class Author(object):
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def __str__(self):
        return self.name

class Book(object):
    def __init__(self,name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name


bukowski = Author("H.Bukowski", 1950)

ozanın_kitabı = Book("Ekmek Arası", 1958, bukowski)
print(type(ozanın_kitabı))

print(ozanın_kitabı.author.name)
print(ozanın_kitabı)
ozanın_kitabı = Book("Ekmek Arası", 1951, bukowski)
print(ozanın_kitabı == ozanın_kitabı2)
print(ozanın_kitabı is ozanın_kitabı2)
