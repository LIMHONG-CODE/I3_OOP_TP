class HundredsCounter:
    """Counts how many complete hundreds are in a non-negative number."""
    def __init__(self, number):
        if number < 0:
            raise ValueError("Number must be non-negative.")

        self.number = number

    def count_hundreds(self):
        return self.number // 100


"""Ask the user for a number and print its complete hundreds."""
try:
    number=int(input("Enter a non-negative Number : "))
    counter = HundredsCounter(number)
    print("Complete Hundreds in the number:", counter.count_hundreds())
except ValueError as e:
    print("Error : ", e)

        