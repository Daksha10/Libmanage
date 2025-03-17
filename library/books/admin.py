from django.contrib import admin
from .models import Book, BorrowedBook, Student  # Use BorrowedBook instead of Borrow

admin.site.register(Book)
admin.site.register(BorrowedBook)  # Corrected name
admin.site.register(Student)
