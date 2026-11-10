class Greeting:
    
    def __init__(self, name):
        self.name = name 

    def say_hello(self):
        print(f"Hello, {self.name} !")

def main():
    name = input("Enter your name -> ").strip()

    greeting = Greeting(name)
    greeting.say_hello()

if __name__ == "__main__":
    main()