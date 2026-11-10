class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calculate_parimeter(self):
                if self.width == 0:
                    print(f"Width is invalid value !")

                P = 2*(self.width + self.height)
                return P

    def calculate_area(self):
            if self.height == 0 :
              print(f"Height is invalid value !")

            A = self.width * self.height
            return A
    
    def display_result(self):

          print(f"Parimeter -> {self.calculate_parimeter()}")
          print(f"Area -> {self.calculate_area()}")

def fix_number(message):
      while True:
            try:
                  return float(input(message))
            except ValueError:
                  print(f"Enter a valeu of width or height again please !")

def main():
    width = fix_number("Enter a value of width -> ")
    height = fix_number("Enter a value of height -> ")

    try:
        rectangle = Rectangle(width, height)

    except ValueError as error:
          print(f"Error -> {error}")
    else:
          rectangle.display_result()

if __name__ == "__main__":
      main()