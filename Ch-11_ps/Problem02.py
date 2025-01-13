class animals:
    pass

class pets(animals):
    pass

class dogs(pets):
    @staticmethod
    def bark():
        print("bhow bhow")

d = dogs.bark()