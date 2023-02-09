class Library:
  bookName = ""
  
  def __init__(self):
    self.books = []
    self.students = []

  def add_book(self, book):
    self.books.append(book)

  def add_student(self, student):
    self.students.append(student)

  def borrow_book(self, student, book):
    if not book.borrowed:
      book.borrowed = True
      student.books.append(book)
      print(f"{student.name} has successfully borrowed {book.title}.")
    else:
      print(f"{book.title} is not available for borrowing.")

  def return_book(self, student, book):
    if book in student.books:
      student.books.remove(book)
      book.borrowed = False
      print(f"{student.name} has successfully returned {book.title}.")
    else:
      print(f"{student.name} did not borrow {book.title}.")

      print(f"{book.title} is not available for borrowing.")


  #def search(self,bookn):
    
  def search(self, searchBook):
    choice = input("If you would like to search by title type 't', by author type a, ")
    for book in self.books:
      if book.title == searchBook:
        print("book exists")



    
  