# Создайте класс «Книга», который имеет атрибуты название, автор и количество страниц.
# Добавьте методы для чтения и записи книги.

import pickle
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Название: {self.title}, Автор: {self.author}, Количество страниц: {self.pages}"

def save_books(book_list):
    with open('books_data.pkl', 'wb') as f:
        pickle.dump(book_list, f)

def load_books():
    try:
        with open('books_data.pkl', 'rb') as f:
            book_list = pickle.load(f)
        return book_list
    except FileNotFoundError:
        return []

book1 = Book("1984", "Джордж Оруэлл", 328)
book2 = Book("Преступление и наказание", "Фёдор Достоевский", 671)

books = [book1, book2]
save_books(books)

loaded_books = load_books()
for book in loaded_books:
    print(book)
