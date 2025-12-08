class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: {self.city}, {self.street}, {self.zip_code}, open: {self.open_hours}, tel: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}, hired: {self.hire_date}, born: {self.birth_date}, address: {self.city}, {self.street}, {self.zip_code}, tel: {self.phone}"


class Student:
    def __init__(self, first_name, last_name, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, address: {self.city}, {self.street}, {self.zip_code}, tel: {self.phone}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}, published: {self.publication_date}, pages: {self.number_of_pages}, {self.library}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n   ".join(str(book) for book in self.books)
        return f"Order date: {self.order_date}\nEmployee: {self.employee}\nStudent: {self.student}\nBooks:\n   {books_str}"


lib1 = Library("Katowice", "Mickiewicza 10", "40-001", "8:00-18:00", "123-456-789")
lib2 = Library("Kraków", "Długa 5", "30-002", "9:00-17:00", "987-654-321")

emp1 = Employee("Jan", "Kowalski", "2020-01-15", "1990-05-10", "Katowice", "Mickiewicza 12", "40-001", "111-222-333")
emp2 = Employee("Anna", "Nowak", "2019-03-20", "1985-07-22", "Kraków", "Długa 7", "30-002", "444-555-666")
emp3 = Employee("Piotr", "Wiśniewski", "2021-06-01", "1992-11-30", "Katowice", "Słoneczna 3", "40-002", "777-888-999")

stud1 = Student("Kasia", "Malinowska", "Katowice", "Słoneczna 4", "40-002", "222-333-444")
stud2 = Student("Tomek", "Lewandowski", "Kraków", "Karmelicka 8", "30-003", "555-666-777")
stud3 = Student("Ola", "Zielińska", "Katowice", "Kościuszki 15", "40-003", "888-999-000")

book1 = Book(lib1, "2001", "Adam", "Mickiewicz", 300)
book2 = Book(lib1, "1999", "Henryk", "Sienkiewicz", 450)
book3 = Book(lib2, "2010", "Wisława", "Szymborska", 200)
book4 = Book(lib2, "2015", "Stanisław", "Lem", 350)
book5 = Book(lib1, "2020", "Olga", "Tokarczuk", 400)

order1 = Order(emp1, stud1, [book1, book2, book5], "2025-11-20")
order2 = Order(emp2, stud2, [book3, book4], "2025-11-21")

print(order1)
print("\n" + "-" * 50 + "\n")
print(order2)
