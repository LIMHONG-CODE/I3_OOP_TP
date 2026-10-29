class EquationCalculator: #Creat class name "EquationCalculator"
    def __init__(self, y, z): #Constructor initializes the values of y and z
        self.y = y #store the input values
        self.z = z 

    def calculate_x(self): #Creat the method to 'calculate x" by using the formula
        if self.y == 0 or self.z == 0: #Using condition to identify y, z > 0
             raise ValueError("y and z must not be zero.") #Manually trigger exception(error)
        if self.y + self.z == 0: #Identify y + z > 0
            raise ValueError("y + z must not be zero")
        x = (self.y * self.z)/(self.y + self.z) #Method of equation
        return x #sent the calculate result back to the caller 

    def display_result(self): #Creat method to display x
        x = self.calculate_x() #Call function calculate_x
        print(f"x = {x}") #Display value of x

try: #Using try block lets you test a block of code errors
    #Get input from user 
    y = float(input("Enter a value of y: "))
    z = float(input("Enter a value of z: "))

     #Creat  calculator object 
    calculator = EquationCalculator(y, z)

    calculator.display_result() #Display the result
except ValueError: #Using except block lets you handle the error
    print("Error: Please enter the valid number!") 