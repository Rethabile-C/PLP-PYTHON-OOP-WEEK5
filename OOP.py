#ASSIGNMENT 1

class Book:
    def __init__(self, title, author, total_pages):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = 1


    def read(self, pages=1):
       self.current_page += pages
       if self.current_page > self.total_pages:
           self.current_page = self.total_pages
           print(f"Reading {self.title} by {self.author}. You have finished the book!")

           class Book:
            class EBook(Book):
             def __init__(self, title, author, total_pages, file_size):
              super().__init__(title, author, total_pages)
              self.file_size = file_size

    def read(self, pages=1):
        super().read(pages)
        print(f"Reading {self.title} by {self.author} on your e-reader. File size: {self.file_size}MB")


#ACTIVITY 2

class Vehicle:
    def move(self):
        print("The vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("The car is driving on the road")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying in the sky")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing on the water")

vehicle = [Car(), Plane(), Boat()]
for v in vehicle:
    v.move()

    