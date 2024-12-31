#1
class Book:

    def __init__(self, title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f'Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}'

book = Book("Война и мир", "Лев Толстой", 1863 )
print(book.get_info())

#2
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Создан объект Circle с радиусом: {self.get_radius()}"

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius
        return f'Радиус был изменён на значение: {self.radius}'


rad = Circle(10)
print(str(rad))
print("Радиус: ",  rad.get_radius())
print(rad.set_radius(44))

