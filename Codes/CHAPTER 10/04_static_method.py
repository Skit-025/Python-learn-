"""This will use a self parameter  that will help to access a method inside a class or we can say it will validate a method in side a class"""
class warriors:
    type="Assian"
    weapon="sword"
    grade="A"
    origin="india"
    @staticmethod
    def greetings(): # These are otherwise called as decorators(Static method)
        return print("Welcome to the world of hunters!")
    def details_collector(self):
        return print(f"Hunter type: {self.type} ,Hunter\'s weapon: {self.weapon} ,Hunter\'s rank:{self.grade} ,Hunter\'s origin:{self.origin}")
Suho=warriors()
Suho.grade='National'
warriors.greetings()
warriors.details_collector(Suho)
"""The upper lie is== Suho.details_collector()"""