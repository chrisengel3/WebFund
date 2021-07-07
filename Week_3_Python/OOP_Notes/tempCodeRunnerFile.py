class Dog:
    # CONSTRUCTOR FUNCTION
    def __init__(self, name, age, hair_color):
        # ATTRIBUTES (the date inside an object)
        self.name = name
        self.age = age
        self.hair_color = hair_color

    # METHODS ARE FUNCTIONS THAT IS PART OF A CLASS
    def bark(self):
        print(f"BORF BOOFIN my name is {self.name}!")

    # ONE WAY TO CALL THE INFO OF THE OBJECT
    def __repr__(self):
        print(f"--Name: {self.name}, Age: {self.age}, Hair Color: {self.hair_color}.")
        return f"--Name: {self.name}, Age: {self.age}, Hair Color: {self.hair_color}."
    # CAN ALSO DO print(dog1.__dict__)

# CREATE AN INSTANCE OF THIS CLASS (AN OBJECT)
# INSTANTIATE

dog1 = Dog("Vicky", 3, "brindle")                                   # BOTH OF THESE #
dog2 = Dog(name = "Leia", age= 0, hair_color = "red and white")     # ARE THE SAME #
print(dog1.name)
print(dog1.age)
print(dog2.name)
print(dog2.age)
dog1.bark()
dog2.bark()
print(dog1.__dict__)
dog1.__repr__()
