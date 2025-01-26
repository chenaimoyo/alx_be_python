Dive into Python Magic Methods
mandatory
Objective: Master Python magic methods by implementing a Book class that incorporates constructors (__init__), destructors (__del__), and the representation methods (__str__ and __repr__).

Task Description:

Create a Python script named book_class.py. In this script, define a Book class that uses specific magic methods to enhance its functionality. This class will model a book with attributes for the title, author, and publication year.

Requirements for Book Class in book_class.py:

Attributes:

title (str): The title of the book.
author (str): The author of the book.
year (int): The publication year of the book.
Magic Methods:

Constructor (__init__): Initializes a Book instance with title, author, and year.
Destructor (__del__): Prints "Deleting (title of the book)" upon object deletion.
String Representation (__str__): Returns a string in the format "(title) by (author), published in (year)".
Official Representation (__repr__): Returns a string that would recreate the Book instance: f"Book('{self.title}', '{self.author}', {self.year})".
Provided for Testing: main.py

To test your Book class, use the following main.py script, which demonstrates creating a Book instance and utilizing the implemented magic methods:


Objective: Deepen your understanding of inheritance and composition in Python by creating a system that models a library with different types of books.

Task Description:

Develop two Python scripts: library_system.py and main.py. In library_system.py, you’ll define a base class Book and two derived classes, EBook and PrintBook, showcasing inheritance. Additionally, implement a Library class demonstrating composition by managing a collection of books.

library_system.py:

Base Class - Book:

Attributes: title (str) and author (str).
Method: __init__(self, title, author) for initializing book attributes.
Derived Classes - EBook and PrintBook:

Both classes inherit from Book.
EBook additional attribute: file_size (int).
PrintBook additional attribute: page_count (int).
Each derived class should have its own __init__ method that properly calls the base class __init__ while also initializing its unique attribute.
Composition - Library:

Attributes: books (a list to store instances of Book, EBook, and PrintBook).
Methods:
add_book(self, book): Adds a Book, EBook, or PrintBook instance to the library.
list_books(self): Prints details of each book in the library.
main.py (Provided for Testing):

This script tests the functionality of your classes in library_system.py by adding different types of books to a Library instance and listing them.





Objective: Enhance your understanding of polymorphism in Python by creating a set of classes that demonstrate method overriding and polymorphic behavior.

Task Description:

You are tasked with creating a Python script named polymorphism_demo.py. In this script, define a base class Shape with a method area() and derived classes Rectangle and Circle, each overriding the area() method to calculate their respective areas.

polymorphism_demo.py:

Base Class - Shape:

Method: area(self), which simply raises a NotImplementedError, indicating that derived classes need to override this method.
Derived Class - Rectangle:

Inherits from Shape.
Attributes: length and width.
Overrides the area() method to calculate the rectangle’s area using the formula: length × width.
Derived Class - Circle:

Inherits from Shape.
Attributes: radius.
Overrides the area() method to calculate the circle’s area using the formula: π × radius² (use math.pi for π).
main.py (Provided for Testing):

This script demonstrates polymorphism by creating instances of Rectangle and Circle, invoking their area() method, and showing that each class calculates the area according to its shape.




Objective: Enhance your understanding of polymorphism in Python by creating a set of classes that demonstrate method overriding and polymorphic behavior.

Task Description:

You are tasked with creating a Python script named polymorphism_demo.py. In this script, define a base class Shape with a method area() and derived classes Rectangle and Circle, each overriding the area() method to calculate their respective areas.

polymorphism_demo.py:

Base Class - Shape:

Method: area(self), which simply raises a NotImplementedError, indicating that derived classes need to override this method.
Derived Class - Rectangle:

Inherits from Shape.
Attributes: length and width.
Overrides the area() method to calculate the rectangle’s area using the formula: length × width.
Derived Class - Circle:

Inherits from Shape.
Attributes: radius.
Overrides the area() method to calculate the circle’s area using the formula: π × radius² (use math.pi for π).
main.py (Provided for Testing):

This script demonstrates polymorphism by creating instances of Rectangle and Circle, invoking their area() method, and showing that each class calculates the area according to its shape.
