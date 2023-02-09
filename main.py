from Book import Book
from Library import Library
from Student import Student
# create books
book1 = Book("One Room Is Not Enough", "Sultan Al Amimi", "987309873")
book2 = Book("Dubai Tales", "Mohammad Al Murr", "938777584")


# create students

student1 = Student("Ahmad", 11)
student2 = Student("Jasim", 12)

# create library and add books and students
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_student(student1)
library.add_student(student2)

# test borrowing and returning books
library.borrow_book(student1, book1)

# Output: Ahmad has successfully borrowed One Room Is Not Enough.
library.borrow_book(student2, book1)


# Output: One Room Is Not Enough is not available for borrowing.
library.return_book(student1, book1)

# Output: Ahmad has successfully returned One Room Is Not Enough.

library.search("One Room Is Not Enough")

print("""




""")